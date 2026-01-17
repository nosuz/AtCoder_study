package abc440;

/*
* E - Cookies
* https://atcoder.jp/contests/abc440/tasks/abc440_e
*
* Test command: gradle test --tests ETest
* Test command: gradle test --tests ETest.sample1
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class E {

    static PriorityQueue<Long> values = new PriorityQueue<>();
    // PriorityQueue<>(Comparator.reverseOrder());
    static long[] A;
    static int X;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        X = sc.nextInt();

        A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        sc.close();

        Arrays.sort(A);
        // System.out.println(Arrays.toString(A));

        int n = N - 1;
        long value = A[n] * K;
        // System.out.println("Best Taste:" + value);
        // Best taste
        values.add(value);

        if (n > 0) {
            for (int i = 1; i <= K; i++) {
                // System.out.println("Change " + i + " of " + A[n] + " by " + A[n - 1]);
                boolean result = change(n - 1, i, value - A[n] * i);
                if (!result) {
                    // これ以上置換しても最低基準を満たさない。
                    // System.out.println("stop");
                    break;
                }
            }
        }

        // System.out.println(values);
        ArrayList<Long> results = new ArrayList<>();
        while (!values.isEmpty()) {
            results.add(values.poll());
        }
        results.sort(Comparator.reverseOrder());

        for (long v : results) {
            System.out.println(v);
        }
    }

    static boolean change(int n, int k, long value) {
        // Return true: changeable

        // A[n]にk枚のクッキーに交換
        // System.out.println(n + "," + k + "," + value);
        // ここで全部消費する
        value += A[n] * k;
        // System.out.println("Taste:" + value);
        if ((values.size() >= X) && (value <= values.peek())) {
            return false;
        } else {
            values.add(value);
            // keep top X values
            while (values.size() > X)
                values.poll();
        }

        if (n > 0) {
            for (int i = 1; i <= k; i++) {
                // System.out.println("Change " + i + " of " + A[n] + " by " + A[n - 1]);
                boolean result = change(n - 1, i, value - A[n] * i);
                if (!result) {
                    // これ以上置換しても最低基準を満たさない。
                    break;
                }
            }
        }

        return true;
    }

}
