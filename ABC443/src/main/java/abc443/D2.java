package abc443;

import java.util.Scanner;

/*
* D - Pawn Line
* https://atcoder.jp/contests/abc443/tasks/abc443_d
*
* Test command: gradle test --tests D2Test
* Test command: gradle test --tests D2Test.sample1
*/

/*
1
5
5 2 1 3 4

1
3
1 3 1

1
20
7 4 6 2 15 5 17 15 1 8 18 1 5 1 12 11 2 7 8 14

*/

public class D2 {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int T = con.nextInt();
        for (int t = 0; t < T; t++) {
            int N = con.nextInt();
            int R[] = new int[N];
            for (int n = 0; n < N; n++) {
                R[n] = con.nextInt();
            }
            // System.out.println(Arrays.toString(R));

            // 局所的最小から右に向かって斜めに積み上げる。
            int toR[] = new int[N];
            toR[0] = R[0];
            for (int i = 1; i < N; i++) {
                toR[i] = Math.min(R[i], toR[i - 1] + 1);
            }

            // 局所的最小から左に向かって斜めに積み上げる。
            int toL[] = new int[N];
            toL[N - 1] = R[N - 1];
            for (int i = N - 2; i >= 0; i--) {
                toL[i] = Math.min(R[i], toL[i + 1] + 1);
            }

            long steps = 0;
            for (int i = 0; i < N; i++) {
                // 左右に向かう斜め線の小さいほうが答え。
                int min = Math.min(toL[i], toR[i]);
                steps += R[i] - min;
            }

            System.out.println(steps);
        }

        con.close();

    }

}
