package abc443;

/*
* C - Chokutter Addiction
* https://atcoder.jp/contests/abc443/tasks/abc443_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

// https://atcoder.jp/contests/abc443/tasks/abc443_c

import java.util.Scanner;

public class C {

	public static void main(String[] args) {
		Scanner con = new Scanner(System.in);

		int N = con.nextInt();
		int T = con.nextInt();

		int A[] = new int[N];
		for (int n = 0; n < N; n++) {
			A[n] = con.nextInt();
		}

		con.close();

		int time = 0;

		int t = 0;
		for (int i = 0; i < N; i++) {

			if (A[i] > t) {
				time += A[i] - t;
				t = A[i] + 100;
			}
		}

		if (T > t)
			time += T - t;

		System.out.println(time);
	}

}
