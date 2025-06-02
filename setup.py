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
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
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


def save_examples_to_file(problem_id, url, examples, template, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f'{problem_id}.py')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template.render(examples=examples, problem_url=url))


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


def create_gitignore(problem_files, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, '.gitignore')

    with open(filename, "w", encoding="utf-8") as f:
        for problem_file in problem_files:
            f.write(f"# {problem_file}\n")


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

    # wait login
    top_page = "https://atcoder.jp/home"
    driver.get(top_page)
    try:
        # 10秒間待って、見つからなければ例外
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.user-gray.bold"))
        )
    except TimeoutException:
        home = os.environ["HOME"]
        print("Login is required by the user. Exec the next command and login")
        print(
            f"google-chrome --user-data-dir={home}/reposit/google-chrome-config --profile-directory=Default")
        exit()

    contest_id_lower = contest_id_upper.lower()
    contest_info = get_contest_info(driver, contest_id_lower)

    out_dir = re.sub(r'([A-Z])(\d)', r'\1_\2', contest_id_upper)
    task_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # task_suffixes = ['a', 'b', 'c', 'd']
    base_url = f'https://atcoder.jp/contests/{contest_id_lower}/tasks/'

    problems = []
    problem_files = []
    for suffix in task_suffixes:
        problem_id = f'{contest_id_lower}_{suffix}'
        task_url = base_url + problem_id
        print(f'取得中: {problem_id} ...')

        try:
            contents = extract_all_examples(driver, task_url)
            problems.append({"title": contents["title"], "url": task_url})
            examples = contents["examples"]
            if examples:
                problem_file = f'{problem_id.upper()}.py'
                save_examples_to_file(
                    problem_id.upper(), task_url, examples, template_problem, out_dir)
                print(f' → {out_dir}/{problem_file} に保存しました')
                problem_files.append(problem_file)
            else:
                print(' → 入力例・出力例が見つかりませんでした')
        except Exception as e:
            print(f'エラーが発生しました: {e}')

    # write .gitignore
    create_gitignore(problem_files, out_dir)

    # make README
    readme_content = {"contest": contest_info["title"], "date": contest_info["date"],
                      "url": contest_info["url"], "problems": problems}
    create_readme(readme_content, template_readme, out_dir)

    # return to the first problem
    driver.get(base_url + f'{contest_id_lower}_{task_suffixes[0]}')
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AtCoder問題の入力例と出力例を収集します。')
    parser.add_argument('contest_id', help='対象のコンテストID（例: abc402 や ABC402）')
    args = parser.parse_args()

    # debugging-port option doesn't work anymore if the profile is under default config directory.
    home = os.environ["HOME"]
    os.system(
        f"google-chrome --remote-debugging-port=9222 --user-data-dir={home}/reposit/google-chrome-config --profile-directory=Default 2> /dev/null&")
    time.sleep(3)
    contest_id_upper = args.contest_id.upper()
    scrape_and_save_all_tasks(contest_id_upper)
