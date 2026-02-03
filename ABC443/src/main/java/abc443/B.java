package abc443;

/*
* B - Setsubun
* https://atcoder.jp/contests/abc443/tasks/abc443_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int N = con.nextInt();
        int K = con.nextInt();

        con.close();

        // 実際に試すスタンダードな方法
        // int n;
        // int k;
        // for (n = N, k = 0; k < K; n++) {
        // k += n;
        // // System.out.println("n:" + n + " k:" + k);
        // }
        // System.out.println(n - N - 1);

        // O(1)の方法
        if (N >= K) {
            System.out.println(0);
            return;
        }

        double b = -0.5 - N;
        double sq = Math.sqrt((0.5 + N) * (0.5 + N) + 2 * (K - N));
        double y = b + sq;
        // System.out.println("y:" + y + " b:" + b + " sq:" + sq);

        System.out.println((int) Math.ceil(y));
    }

}
