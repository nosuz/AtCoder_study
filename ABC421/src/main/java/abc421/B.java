package abc421;

/*
* B - Fibonacci Reversed
* https://atcoder.jp/contests/abc421/tasks/abc421_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

// int の最大値に注意が必要。

import java.util.Scanner;

public class B {

    static long revert(long x) {
        String x_str = Long.toString(x);

        String result = "";
        for (int i = x_str.length() - 1; i >= 0; i--) {
            result += x_str.charAt(i);
        }

        return Long.parseLong(result);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long X = sc.nextInt();
        long Y = sc.nextInt();

        sc.close();

        for (int i = 2; i < 10; i++) {
            long tmp = Y;
            Y = revert(X + Y);
            X = tmp;
        }
        System.out.println(Y);

    }
}
