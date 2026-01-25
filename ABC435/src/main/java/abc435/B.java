package abc435;

/*
* B - No-Divisible Range
* https://atcoder.jp/contests/abc435/tasks/abc435_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int A[] = new int[N + 1];
		int sum[] = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			A[i] = sc.nextInt();
			sum[i] = A[i] + sum[i - 1];
		}
//		for (int i : sum) {
//			System.out.println(i);
//		}

		sc.close();

		// 累積を作っておいて、ループする
		int count = 0;
		for (int l = 1; l <= N; l++) {
			for (int r = l; r <= N; r++) {
				int total = sum[r] - sum[l - 1];
//				System.out.printf("l: %d, r: %d, sum: %d%n", l, r, total);

				boolean mod = true;
				// 約数が含まれるか調べる
				for (int i = l; i <= r; i++) {
					if (total % A[i] == 0) {
						mod = false;
						break;
					}
				}
				if (mod)
					count += 1;
			}

		}

		System.out.println(count);
	}

}
