package abc430;

/*
* A - Candy Cookie Law
* https://atcoder.jp/contests/abc430/tasks/abc430_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int A = con.nextInt();
        int B = con.nextInt();
        int C = con.nextInt();
        int D = con.nextInt();

        con.close();

        if (C >= A) {
            // 法律の規定を満たすか確認
            if (D >= B) {
                System.out.println("No");
            } else {
                System.out.println("Yes");
            }
        } else {
            System.out.println("No");
        }
    }

}
