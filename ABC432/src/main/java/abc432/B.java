package abc432;

/*
* B - Permute to Minimize
* https://atcoder.jp/contests/abc432/tasks/abc432_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/
// オムロンプログラミングコンテスト2025 #2（AtCoder Beginner Contest 432） B問題
// https://atcoder.jp/contests/abc432/tasks/abc432_b

import java.util.Arrays;
import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        String line = con.nextLine();
        con.close(); // 使ったら閉じる
        // System.out.println(line);

        char[] str = line.toCharArray();
        Arrays.sort(str); // 小さい順に並ぶ。
        // 0が来た時にどうするか？
        if (str[0] == '0') {
            // 0以外を頭に持ってくる
            char tmp;
            for (int j = 1; j < str.length; j++) {
                if (str[j] != '0') {
                    tmp = str[0];
                    str[0] = str[j];
                    str[j] = tmp;
                    break;
                }
            }

        }
        for (int j = 0; j < str.length; j++) {
            System.out.print(str[j]);
        }
        System.out.println("");

    }

}
