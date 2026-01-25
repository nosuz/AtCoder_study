package abc434;

/*
* A - Balloon Trip
* https://atcoder.jp/contests/abc434/tasks/abc434_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int W = sc.nextInt(); // unit kg
		int B = sc.nextInt(); // unit g

		sc.close();

		System.out.println(W * 1000 / B + 1); // 割り切れた時、バランスしていたら飛べない
	}

}
