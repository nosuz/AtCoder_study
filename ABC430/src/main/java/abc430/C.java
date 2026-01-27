package abc430;

/*
* C - Truck Driver
* https://atcoder.jp/contests/abc430/tasks/abc430_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Scanner;

/*

5 2 1
aaaaa
expected: 3

12 4 2
abbaaabaabab
expected: 3

11 4 2
abbaaabaaba
expected: 3

2 1 2
ab
expected: 2

 */

public class C {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int N = con.nextInt();
        int A = con.nextInt();
        int B = con.nextInt();

        String S = con.next();
        // System.out.println(S);

        con.close();

        int i = 0, ia = 0, ib = 0;
        int count_a = 0;
        int count_b = 0;
        long result = 0;

        while (i < N) {
            // find the limit of A
            while ((ia < N) && (count_a < A)) {
                if (S.charAt(ia) == 'a') {
                    count_a += 1;
                }
                ia += 1;
            }

            // find the limit of B
            while ((ib < N) && (count_b < B)) {
                if (S.charAt(ib) == 'b') {
                    count_b += 1;
                }
                ib += 1;
            }

            // count
            // System.out.println("i:" + i + " a:" + ia + "(" + count_a + ") b:" + ib + "("
            // + count_b + ")");
            if (count_a >= A) {
                if (count_b < B) {
                    // Bになる前にループを抜けているということは、Bになる前にibが右端に達している。
                    result += N - ia + 1;
                } else if (ib > ia) {
                    result += ib - ia;
                }
            }

            // 左を一つ進める。
            if (S.charAt(i) == 'a') {
                count_a -= 1;
            } else {
                count_b -= 1;
            }

            i += 1;
        }

        System.out.println(result);
    }

}
