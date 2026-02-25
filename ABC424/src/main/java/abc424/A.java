package abc424;

/*
* A - Isosceles
* https://atcoder.jp/contests/abc424/tasks/abc424_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt(); // a
        int b = sc.nextInt(); // b
        int c = sc.nextInt(); // c

        sc.close();

        if ((a == b) || (b == c) || (c == a)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
