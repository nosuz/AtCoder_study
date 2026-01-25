package abc433;

/*
* B - Nearest Taller
* https://atcoder.jp/contests/abc433/tasks/abc433_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 人数
		int[] A = new int[N];
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt(); // 身長
		}

		sc.close();

		// B問題なので、二重ループしてもOKだろう
		for (int i = 0; i < N; i++) {
			int taller = -1;
			for (int j = i; j >= 0; j--) {
				// 調べるところから左に見てゆく
				if (A[j] > A[i]) {
					// 背が高い人を見つけた
					taller = j + 1;
					break; // 次に行く
				}
			}
			// for をやり遂げたら、背が高い人がいない。
			System.out.println(taller);
		}

	}

}
