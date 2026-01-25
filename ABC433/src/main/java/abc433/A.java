package abc433;

/*
* A - Happy Birthday! 4
* https://atcoder.jp/contests/abc433/tasks/abc433_a
*
* Test command: gradle test --tests ATest
* Test command: gradle test --tests ATest.sample1
*/

import java.util.Scanner;

public class A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int X = sc.nextInt(); //
		int Y = sc.nextInt(); // X >= Y という条件はないが、XがYの倍数になるのでこの条件があるはず。
		int Z = sc.nextInt(); // 倍数 2 <= X <= 10

		sc.close();

		// A問題なので、甘く見て条件を満たす年があるか適当に試してみる。
		for (int i = 0; i < 100; i++) {
			if (((X + i) / (Y + i)) == Z) {
				if (((X + i) % (Y + i)) == 0) {
					// 整数演算なので、少数にならないことを確認する必要がある。
					System.out.println("Yes");
					return;
				}
			}
		}
		System.out.println("No");

	}

}
