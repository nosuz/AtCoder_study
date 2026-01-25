package abc434;

/*
* D - Clouds
* https://atcoder.jp/contests/abc434/tasks/abc434_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.Scanner;
// ABC434 D - Clouds
// https://atcoder.jp/contests/abc434/tasks/abc434_d

/*
2
2 4 1 4
6 6 2 10

 */

public class D {

	public static void main(String[] args) {
		int size = 2000;
		int area = size * size;

		Scanner sc = new Scanner(System.in);

		// size+1は、お尻の値を入れるため。
		int[][] sky = new int[size + 1][size + 1]; // 0で初期化されているはず。
		int[][] cloud = new int[size + 1][size + 1];
		int N = sc.nextInt();
		for (int id = 1; id <= N; id++) {
			// -1 to fit array
			int U = sc.nextInt() - 1;
			int D = sc.nextInt() - 1;
			int L = sc.nextInt() - 1;
			int R = sc.nextInt() - 1;

			// 二次元imos
			sky[U][L] += 1;
			sky[U][R + 1] -= 1;
			sky[D + 1][R + 1] += 1;
			sky[D + 1][L] -= 1;
			// 雲の情報も二次元imosする。
			// その結果、雲が1つの場所を見ると、cloudにはその雲の元となった雲のID（番号）が入っている。
			cloud[U][L] += id;
			cloud[U][R + 1] -= id;
			cloud[D + 1][R + 1] += id;
			cloud[D + 1][L] -= id;

		}

		sc.close();

		// rowの晴れを事前計算する
		int covered = 0;
		// 横方向スキャン
		for (int r = 0; r < size; r++) {
			int sum_sky = 0;
			int cloud_id = 0;
			for (int c = 0; c < size; c++) {
				sum_sky += sky[r][c];
				sky[r][c] = sum_sky;
				cloud_id += cloud[r][c];
				cloud[r][c] = cloud_id;
			}
		}
		// 縦方向へスキャン
		for (int c = 0; c < size; c++) {
			int sum_sky = 0;
			int cloud_id = 0;
			for (int r = 0; r < size; r++) {
				sum_sky += sky[r][c];
				sky[r][c] = sum_sky;
				cloud_id += cloud[r][c];
				cloud[r][c] = cloud_id;
				if (sum_sky > 0)
					covered += 1;
			}
		}

		// debug
//		System.out.println("sky -----------");
//		for (int r = 0; r < size; r++) {
//			for (int c = 0; c < size; c++) {
//				System.out.printf("%02d ", sky[r][c]);
//			}
//			System.out.println();
//		}
//		System.out.println("---------------");

		int[] clouds = new int[N + 1];
		for (int r = 0; r < size; r++) {
			for (int c = 0; c < size; c++) {
				if (sky[r][c] == 1) {
					clouds[cloud[r][c]] += 1;
				}
			}
		}

		for (int id = 1; id <= N; id++) {
			System.out.println(area - (covered - clouds[id]));
		}

	}

}
