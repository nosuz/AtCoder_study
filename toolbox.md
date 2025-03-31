## サンプルデータの読み込み

サンプルをコピペして標準入力から読み込ませるのはめんどくさい。

- StringIO を使用する。
- 環境変数を参照して、ローカルと提出環境を判断する。

仮想環境を作成する。

```bash
sudo apt update
sudo apt install python3.12-venv
python3 -m venv ~/.at_coder
. ~/.at_coder/bin/activate
pip install dotenv
```

.env に環境変数を設定する。

```
LOCAL_DEBUG=T
```

プログラムに環境変数で標準入力を読むか・サンプルデータを読むか分岐するコードを入れる。

```python
import io
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()  # .env
except ModuleNotFoundError:
    pass  # ignore no dotenv error

TEST_DATA = """
6
abcarc
agcahc

7
atcoder
contest

"""

if os.getenv("LOCAL_DEBUG"):
    # trim \n and blank lines
    sys.stdin = io.StringIO(TEST_DATA[1:].replace('\n\n', '\n'))


def code():
    pass

if os.getenv("LOCAL_DEBUG"):
    while True:
        try:
            code()
        except EOFError:
            break
else:
    code()

```

### 標準入力から読み込み

```python
a = input()

print(a)
```

### 標準入力から数値を読み込み

```python
a = int(input())

print(a + 1)
```

### 標準入力から空白区切りで複数項目を読み込み

```python
a, b = input().split()

print(f"a: {a}, b: {b}")
```

### 標準入力から空白区切りで複数の数値を読み込み

```python
a, b = map(int, input().split())

print(f"a+b: {a + b}")
```
