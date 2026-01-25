package abc437;

/*
* D - Sum of Differences
* https://atcoder.jp/contests/abc437/tasks/abc437_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Number437 {
	long num;
	int count;

	Number437(long num) {
		this.num = num;
		this.count = 1;
	}

	void add() {
		count += 1;
	}

	public String toString() {
		return "" + num + "(" + count + ")";
	}

}

public class D {

	public static void main(String[] args) {
		final boolean DEBUG = false;

		Scanner sc = new Scanner(System.in);

		int M = sc.nextInt(); // 数列Aの数
		int N = sc.nextInt(); // 数列Bの数

		long A[] = new long[M];
		long B[] = new long[N];

		for (int i = 0; i < M; i++) {
			A[i] = sc.nextInt();
		}

		for (int i = 0; i < N; i++) {
			B[i] = sc.nextInt();
		}

		sc.close();

		// 積算して、前後を見ればそれまでの合計が得られる作戦。
		Arrays.sort(A);
		Arrays.sort(B);
		if (DEBUG) {
			// debug
			for (int i = 0; i < M; i++) {
				System.out.print(A[i] + ", ");
			}
			System.out.println();
			for (int i = 0; i < N; i++) {
				System.out.print(B[i] + ", ");
			}
			System.out.println();
		}

		ArrayList<Number437> BB = new ArrayList<>();
		BB.add(new Number437(B[0]));
		for (int i = 1; i < N; i++) {
			if (BB.get(BB.size() - 1).num == B[i]) {
				BB.get(BB.size() - 1).add();
			} else {
				BB.add(new Number437(B[i]));
			}
		}
		if (DEBUG) {
			// debug
			for (int i = 0; i < BB.size(); i++) {
				System.out.print(BB.get(i) + ", ");
			}
			System.out.println();
		}

		long forward_sum[] = new long[BB.size()];
		int forward_count[] = new int[BB.size()];
		long reverse_sum[] = new long[BB.size()];
		int reverse_count[] = new int[BB.size()];
		// init 0
		forward_sum[0] = 0;
		forward_count[0] = BB.get(0).count;
		reverse_sum[BB.size() - 1] = 0;
		reverse_count[BB.size() - 1] = BB.get(BB.size() - 1).count;
		for (int i = 1; i < BB.size(); i++) {
			forward_count[i] = forward_count[i - 1] + BB.get(i).count;
			forward_sum[i] = (forward_sum[i - 1] + (BB.get(i).num - BB.get(i - 1).num) * forward_count[i - 1])
					% 998244353;
		}
		for (int i = (BB.size() - 2); i >= 0; i--) {
			reverse_count[i] = reverse_count[i + 1] + BB.get(i).count;
			reverse_sum[i] = (reverse_sum[i + 1] + (BB.get(i + 1).num - BB.get(i).num) * reverse_count[i + 1])
					% 998244353;
		}

		if (DEBUG) {
			// debug
			for (int i = 0; i < BB.size(); i++) {
				System.out.print(forward_sum[i] + ", ");
			}
			System.out.println();
			for (int i = 0; i < BB.size(); i++) {
				System.out.print(forward_count[i] + ", ");
			}
			System.out.println();
			for (int i = 0; i < BB.size(); i++) {
				System.out.print(reverse_sum[i] + ", ");
			}
			System.out.println();
			for (int i = 0; i < BB.size(); i++) {
				System.out.print(reverse_count[i] + ", ");
			}
			System.out.println();
		}

		long sum = 0;
		int p = 0; // pointer for A
		// left of B
		while (A[p] < BB.get(0).num) {
			if (DEBUG)
				System.out.println("" + p + " Left: " + A[p]);
			sum = (sum + (BB.get(0).num - A[p]) * N + reverse_sum[0]) % 998244353;

			p += 1;
			if (p >= M)
				break;
		}

		// in B range
		int i = 0;
		while ((p < M) && (i < (BB.size() - 1))) {
			if (DEBUG) {
				System.out.println("" + p + "," + i + " " + A[p]);
				System.out.println("i<=p: " + (BB.get(i).num <= A[p]));
				System.out.println("p<i+1: " + (A[p] < BB.get(i + 1).num));
			}
			if ((BB.get(i).num <= A[p]) && (A[p] < BB.get(i + 1).num)) {
				sum = (sum + (A[p] - BB.get(i).num) * forward_count[i] + forward_sum[i]) % 998244353;
				sum = (sum + (BB.get(i + 1).num - A[p]) * reverse_count[i + 1] + reverse_sum[i + 1]) % 998244353;

				p += 1;
				if (DEBUG)
					System.out.println("sum: " + sum);
			} else {
				i += 1;
				if (DEBUG)
					System.out.println("skip");
			}
		}

		// in right
		int last_BB = BB.size() - 1;
		while (p < M) {
			if (DEBUG)
				System.out.println("" + p + " Right: " + A[p]);
			sum = (sum + (A[p] - BB.get(last_BB).num) * forward_count[last_BB] + forward_sum[last_BB]) % 998244353;

			p += 1;
		}

		System.out.println(sum);
	}

}
