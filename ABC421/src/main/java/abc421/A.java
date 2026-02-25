package abc421;

import java.util.HashMap;

/*
* A - Misdelivery
* https://atcoder.jp/contests/abc421/tasks/abc421_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 住人の数
        HashMap<Integer, String> S = new HashMap<>();
        for (int i = 0; i < N; i++) {
            // 部屋番号と住人の対応
            String name = sc.next();
            S.put(i, name);
        }

        // 問い合わせに回答
        int X = sc.nextInt();
        String Y = sc.next();

        if (S.get(X - 1).equals(Y)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();

    }
}
