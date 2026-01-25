package abc435;

/*
* C - Domino
* https://atcoder.jp/contests/abc435/tasks/abc435_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Scanner;

public class C {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int A[] = new int[N];
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
		}

		sc.close();

		int force = A[0] - 1;

		int i = 0;
		while ((i < N) && (force != 0)) {
			force = Math.max(force, A[i]) - 1;
			i += 1;
		}
		System.out.println(i == 0 ? 1 : i);
	}
}
