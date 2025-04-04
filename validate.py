import re
import subprocess
import sys


def extract_test_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    match = re.search(r'"""TEST_DATA(.*?)"""', content, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None


def run_prog_with_data(prog_name, data):
    blocks = data.strip().split("\n\n")  # Split into blocks by empty lines
    for index, block in enumerate(blocks):
        # skip comment outed sample
        if block[0] == '#':
            continue

        try:
            input_data, expected_answer = block.split("#")
            expected_answer = expected_answer.lstrip()
        except ValueError:
            input_data = block
            expected_answer = None
        print(f"Input {index}")
        print(input_data)
        process = subprocess.Popen(["python3", prog_name], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data)
        stdout = stdout.strip()
        print(f"Output {index}")
        print(stdout, stderr)
        if process.returncode != 0:
            break
        elif expected_answer:
            if stdout == expected_answer:
                print("OK")
            else:
                print(f"WA, expected: {expected_answer}")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 validate.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    extracted_data = extract_test_data(filename)
    if extracted_data is not None:
        # Use filename as program name
        run_prog_with_data(filename, extracted_data)
    else:
        print("TEST_DATA not found.")
