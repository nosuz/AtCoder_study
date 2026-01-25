package abc436;

/*
* A - o-padding
* https://atcoder.jp/contests/abc436/tasks/abc436_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 必要な長さ
		String S = sc.next(); // 文字列

		sc.close();

		for (int i = 0; i < (N - S.length()); i++) {
			System.out.print("o");
		}
		System.out.println(S);
	}

}
