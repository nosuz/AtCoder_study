package abc424;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

/*
* B - Perfect
* https://atcoder.jp/contests/abc424/tasks/abc424_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 人数
        int M = sc.nextInt(); // 問題数
        int K = sc.nextInt(); // イベントの数

        HashMap<Integer, HashSet<Integer>> ok = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();
        for (int k = 0; k < K; k++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            if (!ok.containsKey(A))
                ok.put(A, new HashSet<>());
            ok.get(A).add(B);

            if (ok.get(A).size() == M)
                ans.add(A);
        }

        if (ans.size() > 0) {
            // 空白区切りの一行で出力する
            for (var a : ans) {
                System.out.print(a + " ");
            }
            System.out.println();
        }

        sc.close();

    }
}
