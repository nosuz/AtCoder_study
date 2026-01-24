package abc440;

/*
* C - Striped Horse
* https://atcoder.jp/contests/abc440/tasks/abc440_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Scanner;

public class C {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();
            int W = sc.nextInt();

            long C[] = new long[N];
            for (int i = 0; i < N; i++) {
                C[i] = sc.nextLong();
            }

            if (N <= W) {
                System.out.println(0);
            } else {
                int W2 = W * 2;
                long cost[] = new long[W2];

                for (int i = 0; i < N; i++) {
                    cost[i % W2] += C[i];
                }
                // System.out.println(Arrays.toString(cost));

                long min_cost = 0;
                for (int i = 0; i < W; i++) {
                    min_cost += cost[i];
                }
                long tmp = min_cost;
                // System.out.println(tmp);
                for (int i = W; i < (W2 + W - 1); i++) {
                    // System.out.println("add:" + i % W2 + " sub:" + (i + W) % W2);
                    tmp += cost[i % W2] - cost[(i + W) % W2];
                    // System.out.println(tmp);
                    if (min_cost > tmp)
                        min_cost = tmp;
                    // System.out.println(min_cost);
                }
                System.out.println(min_cost);
            }
        }

    }

}
