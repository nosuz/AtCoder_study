package abc434;

/*
* B - Bird Watching
* https://atcoder.jp/contests/abc434/tasks/abc434_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 飛んでいる鳥の数
		int M = sc.nextInt(); // 鳥の種類

		int[] weights = new int[M];
		int[] counts = new int[M];
		int A;
		int B;
		for (int i = 0; i < N; i++) {
			A = sc.nextInt(); // 観察した鳥の種類
			B = sc.nextInt(); // 観察した鳥の重さ

			// 0で初期化されているはず
			// 種類は1始まりに注意
			weights[A - 1] += B;
			counts[A - 1] += 1;
		}

		sc.close();

		// not N but M
		for (int i = 0; i < M; i++) {
			System.out.println((double) weights[i] / counts[i]);
		}
	}

}
