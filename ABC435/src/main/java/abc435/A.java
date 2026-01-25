package abc435;

/*
* A - Triangular Number
* https://atcoder.jp/contests/abc435/tasks/abc435_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		sc.close();

		int total = 0;
		for (int i = 1; i <= N; i++) {
			total += i;
		}

		System.out.println(total);
	}

}
