package abc437;

/*
* A - Feet
* https://atcoder.jp/contests/abc437/tasks/abc437_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt(); // フィート
		int B = sc.nextInt(); // インチ

		sc.close();

		System.out.println(A * 12 + B);
	}

}
