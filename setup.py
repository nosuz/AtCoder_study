#!/usr/bin/env python

import os
import re
import argparse
import time
from datetime import datetime

TEMPLATE_DIR = os.path.dirname(__file__)
TEMPLATE_PROBLEM = "problem_template.py"
TEMPLATE_README = "readme_template.md"

try:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    from jinja2 import Template, FileSystemLoader, Environment
except ModuleNotFoundError:
    print("venv is required. activated by the following command")
    print(" . atcoder/bin/activate")
    exit()


def extract_all_examples(driver, url):
    driver.get(url)
    time.sleep(2)
    response_html = driver.page_source
    soup = BeautifulSoup(response_html, 'html.parser')

    parts = soup.select('div.part')
    examples = []
    title = driver.title

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
                    output_text = pre_output.text.strip().replace('\n', ' ')
                    examples.append((input_text, output_text))
                    i += 2
                    continue
        i += 1

    return {"title": title, "examples": examples}


def get_template(directory, template_name):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    return env.get_template(template_name)


def save_examples_to_file(problem_id, examples, template, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f'{problem_id}.py')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template.render(examples=examples))


def get_contest_info(driver, contest_id_lower):
    contest_url = f'https://atcoder.jp/contests/{contest_id_lower}'
    driver.get(contest_url)
    time.sleep(2)
    response_html = driver.page_source
    soup = BeautifulSoup(response_html, 'html.parser')

    title = soup.select_one(
        '#main-container > div.row > div:nth-child(2) > div.insert-participant-box > div.mb-2 > h1')

    date_part = soup.select_one(
        '#contest-nav-tabs > div > small.contest-duration > a:nth-child(1) > time')

    date_str = re.sub(r'\(.+', '', date_part.get_text(strip=True))
    print(date_str)
    date = datetime.strptime(date_str, "%Y-%m-%d")

    return {"title": title.get_text(strip=True), "date": date.strftime('%Y 年 %-m 月 %-d 日'), "url": contest_url}


def create_readme(contents, template, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, 'README.md')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template.render(contents=contents))


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options


def scrape_and_save_all_tasks(contest_id_upper):
    template_problem = get_template(TEMPLATE_DIR, TEMPLATE_PROBLEM)
    template_readme = get_template(TEMPLATE_DIR, TEMPLATE_README)

    chrome_options = get_default_chrome_options()
    # chrome://version/
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(service=webdriver.ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(2)

    contest_id_lower = contest_id_upper.lower()
    contest_info = get_contest_info(driver, contest_id_lower)

    out_dir = re.sub(r'([A-Z])(\d)', r'\1_\2', contest_id_upper)
    task_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # task_suffixes = ['a', 'b', 'c', 'd']
    base_url = f'https://atcoder.jp/contests/{contest_id_lower}/tasks/'

    problem_titles = []
    for suffix in task_suffixes:
        problem_id = f'{contest_id_lower}_{suffix}'
        task_url = base_url + problem_id
        print(f'取得中: {problem_id} ...')

        try:
            contents = extract_all_examples(driver, task_url)
            problem_titles.append(contents["title"])
            examples = contents["examples"]
            if examples:
                save_examples_to_file(
                    problem_id.upper(), examples, template_problem, out_dir)
                print(f' → {out_dir}/{problem_id.upper()}.py に保存しました')
            else:
                print(' → 入力例・出力例が見つかりませんでした')
        except Exception as e:
            print(f'エラーが発生しました: {e}')

    # make README
    readme_contest = {"contest": contest_info["title"], "date": contest_info["date"],
                      "url": contest_info["url"], "titles": problem_titles}
    create_readme(readme_contest, template_readme, out_dir)

    # return to the first problem
    driver.get(base_url + f'{contest_id_lower}_{task_suffixes[0]}')
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AtCoder問題の入力例と出力例を収集します。')
    parser.add_argument('contest_id', help='対象のコンテストID（例: abc402 や ABC402）')
    args = parser.parse_args()

    print("Close all Chrome browsers.")
    print("Then hit 'Enter'. New Chrome browser will be start for Selenium.")

    print()
    input("Hit 'Enter' when confirmed all Chrome are closed.")
    os.system("google-chrome --remote-debugging-port=9222 2> /dev/null&")
    time.sleep(3)

    contest_id_upper = args.contest_id.upper()
    scrape_and_save_all_tasks(contest_id_upper)
