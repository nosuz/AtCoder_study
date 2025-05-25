## 開催日

2025 年 5 月 24 日

## コンテストページ

[AtCoder Beginner Contest 407（Promotion of AtCoderJobs）](https://atcoder.jp/contests/abc407)

## A - Approximation

四捨五入、ただし組み込み関数の round に注意。

```python
round(1.5) == round(2.5)
```

## B - P(X or Y)

- B 問題なので、計算量を考えずに総当りして条件に合う組み合わせを数え上げる。
- サイコロの(1,2)と(2,1)を区別できないが、区別して確率計算を単純化する。

## C - Security 2

- 桁数は、A ボタンの数で決まる。
- 先頭の数字は繰り返し B ボタンの`+1`操作を受けるので、後ろの桁から考えていく。
- 隣接する数字の差が、B ボタンを押した数になる。

## D - Domino Covering XOR

## E - Most Valuable Parentheses

## F - Sums of Sliding Window Maximum

## G - Domino Covering SUM
