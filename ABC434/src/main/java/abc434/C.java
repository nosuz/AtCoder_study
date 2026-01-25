package abc434;

/*
* C - Flapping Takahashi
* https://atcoder.jp/contests/abc434/tasks/abc434_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Scanner;

class Range {
	long t;
	long min;
	long max;

	Range(long t, long min, long max) {
		this.t = t;
		this.min = min;
		this.max = max;
	}

	Range overlap(Range from) {
		long delta_t = t - from.t;
		long updated_min = from.min - delta_t;
		long updated_max = from.max + delta_t;
//		System.out.println("Updated: " + delta_t + " " + updated_min + " " + updated_max);
//		System.out.println("This: " + this.min + " " + this.max);

		// 高さを0にすることはできない。
		updated_min = (updated_min <= 0) ? 1 : updated_min;
//		max = (max <= 0) ? 1 : max;

		// 更新された範囲で、目標が完全に含まれる場合を考慮できていない。
		if (((this.min <= updated_min) && (updated_min <= this.max))
				|| ((this.min <= updated_max) && (updated_max <= this.max))) {
			long next_min;
			long next_max;

			if (this.min > updated_min) {
				next_min = this.min;
			} else {
				next_min = updated_min;
			}
			if (this.max < updated_max) {
				next_max = this.max;
			} else {
				next_max = updated_max;
			}

			return new Range(this.t, next_min, next_max); // tの時に実際にいる高さの範囲
		} else if ((updated_min <= this.min) && (this.max <= updated_max)) {
			// 更新された範囲が、目標を完全に含む
//			return new Range(this.t, this.min, this.max);
			return this;
		} else {
			return null;
		}
	}
}

public class C {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt(); // case数
		for (int i = 0; i < T; i++) {
			int N = sc.nextInt(); // 目標数
			long H = sc.nextLong(); // 最初の高さ

			Range[] ranges = new Range[N];
			Range range = new Range(0, H, H);
			for (int j = 0; j < N; j++) {
				long t = sc.nextLong(); // 経過時間
				long l = sc.nextLong(); // 下限
				long u = sc.nextLong(); // 上限
				ranges[j] = new Range(t, l, u);
			}
//			for (Range item : ranges) {
//				System.out.println(item.t + " " + item.min + " " + item.max);
//			}
//			System.out.println("---");
//			System.out.println("range: " + range.t + " " + range.min + " " + range.max);

			for (int j = 0; j < N; j++) {
				range = ranges[j].overlap(range);
				if (range == null) {
					// no overlap
					break;
				}
			}
			if (range == null) {
				System.out.println("No");
			} else {
				System.out.println("Yes");
			}
		}

		sc.close();

	}

}
