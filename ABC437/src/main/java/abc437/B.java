package abc437;

/*
* B - Tombola
* https://atcoder.jp/contests/abc437/tasks/abc437_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int H = sc.nextInt(); // 行
		int W = sc.nextInt(); // 列
		int N = sc.nextInt(); // query数

		int[][] matrix = new int[H][W];
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				matrix[i][j] = sc.nextInt();
			}
		}

		int[] B = new int[N];
		for (int i = 0; i < N; i++) {
			B[i] = sc.nextInt();
		}

		sc.close();

		int max = 0;
		for (int i = 0; i < H; i++) {
			int count = 0;
			for (int j = 0; j < W; j++) {
				for (int k = 0; k < N; k++) {
					if (matrix[i][j] == B[k])
						count += 1;
				}
			}
			if (count > max)
				max = count;
		}
		System.out.println(max);

	}

}
