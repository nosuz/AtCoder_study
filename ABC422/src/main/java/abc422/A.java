package abc422;

/*
* A - Stage Clear
* https://atcoder.jp/contests/abc422/tasks/abc422_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();

        sc.close();

        String[] pos = S.split("-");
        int world = Integer.parseInt(pos[0]);
        int stage = Integer.parseInt(pos[1]);
        if (stage < 8) {
            stage += 1;
        } else {
            world += 1;
            stage = 1;
        }

        System.out.printf("%d-%d\n", world, stage);
    }
}
