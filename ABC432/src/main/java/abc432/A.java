package abc432;

/*
* A - Permute to Maximize
* https://atcoder.jp/contests/abc432/tasks/abc432_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Arrays;
import java.util.Scanner;

public class A {
    // AtCoderに提出するときは、Main classにする必要がある。

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        String line = con.nextLine();
        con.close(); // 使ったら閉じる
        // System.out.println(line);

        String[] items = line.split(" "); // 文字列で分割できる。
        int[] num = new int[items.length];
        for (int i = 0; i < items.length; i++) {
            // System.out.println(items[i]);
            num[i] = Integer.parseInt(items[i]);
        }
        // 昇順でソートされる。
        Arrays.sort(num);
        // 最大の数なので、大きい順に出力する。
        for (int i = num.length - 1; i >= 0; i--) {
            System.out.print(num[i]);
        }
        System.out.println("");
    }

}
