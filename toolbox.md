## サンプルデータの読み込み

サンプルをコピペして標準入力から読み込ませるのはめんどくさい。

コード中にサンプルデータをコメントとして埋め込む。

```python
"""TEST_DATA
6
abcarc
agcahc

7
atcoder
contest

"""
```

コードを実行する。

```bash
python3 validate.py ABC_399/A.py
```

### 標準入力から文字列を読み込み

```python
a = input()

a = list(input()) # 文字列を文字配列にする

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
n, m = map(int, input().split())
# TypeError: 'list' object is not callable になった時の対応
a, b, c, d = [int(v) for v in input().split()]
# get list
p = list(map(int, input().split()))

print(f"a+b: {a + b}")
```

### 標準入力から空白区切りで複数の数値を読み込みリスト化する

```python
# l = [a for a in map(int, input().split())]
l = list(map(int, input().split()))

print(l)
```

## ソートする

### List Tuple

```python
l = [(87, 0), (87, 1), (87, 2), (88, 3), (41, 4), (38, 5), (41, 6), (38, 7)]

sorted_l = sorted(l, reverse=False, key=lambda x: x[1])
# reverseがTのときは、max to minになる。
```

### Dict

```python
l = [{"key1": 1, "key2": 2}, {"key1": 4, "key2": 5}, {"key1": 3, "key2": 2}, {"key1": 10, "key2": 1}]

sorted_l = sorted(l, reverse=False, key=lambda x: x["key2"])
# reverseがTのときは、max to minになる。
```

## プログラムを終了させる

```python
exit()
```

## 文字列

### 文字コード

```python
# 文字コード
code = ord("@")
print(code)

code = ord(" ")
print(f"0x{code:x}")

# 数値から文字
char1 = chr(0x20)
char2 = chr(64)
print(f"-{char1}-{char2}-")

```

### 文字列をばらばらにする

```python
list = list("abcd")
print(list)
# ['a', 'b', 'c', 'd']

```

## List型

```python
str = list("01234567")

print(str[:1])
# ['0']
print(str[0:2])
# ['0', '1']

```

### print

Listの内容を印刷する。

```python
str = list("01234567")
print(*str) # default: sep = " "
print(*str, sep="")

num = [0, 1, 2, 3, 4, 5, 6, 7]
print(*num, sep=" ")
```

### enumerate

インデックスと値を一緒に取り出す。Dict型にも使用できる。

```python
num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for index, value in enumerate(num):
    print(f"index: {index}, value: {value}")
```

## Dict型

### defaultdict

初期化無しで使用できるDict型

```python
from collections import defaultdict

d = defaultdict(lambda: 0)
d["a"] += 1
d["b"] = 1
print(d)
```

### each

```python
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

for key, value in my_dict.items():
    print(f"キー: {key}, 値: {value}")
```

## for-else block

```python
for i in range(10):
    if i > 5:
        break
else:
    print("no break only")
    # continue in double for
print(i)

```

## 数値型

### floor ceil

```python
import math

math.floor()
math.ceil()
```
