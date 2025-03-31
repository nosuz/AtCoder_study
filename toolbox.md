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

print(f"a+b: {a + b}")
```
