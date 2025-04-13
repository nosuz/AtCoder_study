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

### リストをソートする

```python
l = [(87, 0), (87, 1), (87, 2), (88, 3), (41, 4), (38, 5), (41, 6), (38, 7)]

sorted_l = sorted(l, reverse=False, key=lambda x: x[1]):
# reverseがTのときは、max to minになる。
```

### プログラムを終了させる

```python
exit()
```
