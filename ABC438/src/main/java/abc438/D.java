package abc438;

import java.util.Arrays;

/*
* D - Tail of Snake
* https://atcoder.jp/contests/abc438/tasks/abc438_d
*
* Test command: gradle test --tests DTest
*/

import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // ステップ数

        long A[] = new long[N];
        long B[] = new long[N];
        long C[] = new long[N];
        // Max of sum is N * A_i
        long a_sum[] = new long[N];
        long b_sum[] = new long[N];
        long c_sum[] = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
            if (i == 0) {
                a_sum[i] = A[i];
            } else {
                a_sum[i] = A[i] + a_sum[i - 1];
            }
        }

        for (int i = 0; i < N; i++) {
            B[i] = sc.nextInt();
            if (i > 0) {
                if (b_sum[i - 1] > a_sum[i - 1]) {
                    b_sum[i] = B[i] + b_sum[i - 1];
                } else {
                    // switch is better
                    b_sum[i] = B[i] + a_sum[i - 1];
                }
            }
        }

        for (int i = 0; i < N; i++) {
            C[i] = sc.nextInt();
            // C は2以上でないと頭とつながらない
            if (i > 1) {
                if (c_sum[i - 1] > b_sum[i - 1]) {
                    c_sum[i] = C[i] + c_sum[i - 1];
                } else {
                    // switch is better
                    c_sum[i] = C[i] + b_sum[i - 1];
                }
            }
        }

        sc.close();

        // System.out.println(Arrays.toString(a_sum));
        // System.out.println(Arrays.toString(b_sum));
        // System.out.println(Arrays.toString(c_sum));
        System.out.println(c_sum[N - 1]);
    }
}
