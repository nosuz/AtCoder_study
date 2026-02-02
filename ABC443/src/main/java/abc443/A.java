package abc443;

/*
* A - Append s
* https://atcoder.jp/contests/abc443/tasks/abc443_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner con = new Scanner(System.in);

		String S = con.next();

		con.close();

		System.out.println(S + "s");

	}

}
