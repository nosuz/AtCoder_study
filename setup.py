#!/usr/bin/env python

import os
import argparse
import requests
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("venv is required. activated by the following command")
    print(" . atcoder/bin/activate")
    exit()


def extract_all_io_examples(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    parts = soup.select('div.part')
    examples = []

    i = 0
    while i < len(parts):
        h3_input = parts[i].find('h3')
        pre_input = parts[i].find('pre')
        if h3_input and '入力例' in h3_input.text and pre_input:
            input_text = pre_input.text.strip()

            if i + 1 < len(parts):
                h3_output = parts[i + 1].find('h3')
                pre_output = parts[i + 1].find('pre')
                if h3_output and '出力例' in h3_output.text and pre_output:
                    output_text = pre_output.text.strip()
                    examples.append((input_text, output_text))
                    i += 2
                    continue
        i += 1

    return examples


def save_examples_to_file(problem_id, examples, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f'{problem_id}.py')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('"""TEST_DATA\n')
        for input_text, output_text in examples:
            excepted_text = output_text.strip().replace('\n', ' ')
            f.write(f'{input_text}\n')
            f.write('<expected>')
            f.write(f' {excepted_text}\n\n')
        f.write('"""\n\n')


def scrape_and_save_all_tasks(contest_id_upper):
    contest_id_lower = contest_id_upper.lower()
    task_suffixes = ['a', 'b', 'c', 'd', 'e', 'f']
    base_url = f'https://atcoder.jp/contests/{contest_id_lower}/tasks/'

    for suffix in task_suffixes:
        problem_id = f'{contest_id_lower}_{suffix}'
        task_url = base_url + problem_id
        print(f'取得中: {problem_id} ...')

        try:
            examples = extract_all_io_examples(task_url)
            if examples:
                save_examples_to_file(
                    problem_id.upper(), examples, out_dir=contest_id_upper)
                print(f' → {contest_id_upper}/{problem_id.upper()}.py に保存しました')
            else:
                print(' → 入力例・出力例が見つかりませんでした')
        except Exception as e:
            print(f'エラーが発生しました: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AtCoder問題の入力例と出力例を収集します。')
    parser.add_argument('contest_id', help='対象のコンテストID（例: abc402 や ABC402）')
    args = parser.parse_args()

    contest_id_upper = args.contest_id.upper()
    scrape_and_save_all_tasks(contest_id_upper)
