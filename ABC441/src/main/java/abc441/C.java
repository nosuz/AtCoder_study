package abc441;

/*
* C - Sake or Water
* https://atcoder.jp/contests/abc441/tasks/abc441_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Arrays;
import java.util.Scanner;

public class C {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        long X = sc.nextLong();

        int A[] = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        sc.close();

        // no way to reverse
        Arrays.sort(A);
        // System.out.println(A[0]);

        long drink = 0;
        for (int i = (K - 1); i >= 0; i--) {
            drink += A[i];
            if (drink >= X) {
                System.out.println(N - i);
                return;
            }
        }
        System.out.println(-1);

    }

}
