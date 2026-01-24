package abc431;

/*
* A - Robot Balance
* https://atcoder.jp/contests/abc431/tasks/abc431_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int H = con.nextInt();
        int B = con.nextInt();
        // System.out.println(H + "-" + B);
        // String line = con.nextLine();
        con.close(); // 使ったら閉じる
        // System.out.println(line);

        if (H > B) {
            System.out.println(H - B);
        } else {
            System.out.println("0");
        }
    }

}
