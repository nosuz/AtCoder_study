## 開催日

2025 年 5 月 17 日

## コンテストページ

[パナソニックグループ プログラミングコンテスト 2025（AtCoder Beginner Contest 406）](https://atcoder.jp/contests/abc406)

## A - Not Acceptable

1. 何時の部分同士を比較して締切の時間よりも前ならば Yes
2. 何時の部分が同じ場合は、何分の単位を比較して締切よりも前ならば Yes
3. それ以外は No

素直に深夜からの経過分に換算して比較や、時刻を 4 桁で表しての比較でも良かったかも。

## B - Product Calculator

桁溢れをどのように検出するかがポイント。

表示可能な桁数が$K$の場合、$Log_{10}{計算結果} >= K$で桁溢れを検出できるはずと思ったが、不正解 (WA) が出てしまった。

そこでもっとプリミティブに $計算結果 >= 10^K$ (提出は$計算結果 > (10^K -1)$)で判断したら正解 (AC)となった。$Log$が WA になった原因が分からない。

他には計算結果を文字列に変換して長さを数える回答例も見た。

## C - ~

## D - Garbage Removal

## E - Popcount Sum 3

## F - Compare Tree Weights

## G - Travelling Salesman Problem
