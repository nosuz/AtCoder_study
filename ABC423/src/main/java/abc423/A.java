package abc423;

/*
* A - Scary Fee
* https://atcoder.jp/contests/abc423/tasks/abc423_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt(); // 残高
        int C = sc.nextInt(); // 1000円当たりの手数料

        sc.close();

        int draw = 0;
        for (int i = (X / 1000); i >= 0; i--) {
            int cost = i * C;
            if (X >= (1000 * i + cost)) {
                draw = 1000 * i;
                break;
            }
        }
        System.out.println(draw);
    }
}
