package abc436;

/*
* B - Magic Square
* https://atcoder.jp/contests/abc436/tasks/abc436_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 辺の長さ

		sc.close();

		int map[][] = new int[N][N];

		// 初期値
		int r = 0;
		int c = (N - 1) / 2;
		int k = 1;

		map[r][c] = k;

		for (int i = 1; i < (N * N); i++) {
			k += 1;

			int new_r = (r - 1) % N;
			if (new_r < 0)
				new_r += N;
			int new_c = (c + 1) % N;
//			System.out.println(new_r + "," + new_c);
			if (map[new_r][new_c] == 0) {
				map[new_r][new_c] = k;
				c = new_c;
			} else {
				new_r = (r + 1) % N;
				map[new_r][c] = k;
			}
//			System.out.println(new_r + "," + new_c);
			r = new_r;
		}

		for (int row = 0; row < N; row++) {
			for (int col = 0; col < N; col++) {
				System.out.print(map[row][col]);
				if (col < (N - 1))
					System.out.print(" ");
			}
			System.out.println();
		}
	}

}
