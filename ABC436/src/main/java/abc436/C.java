package abc436;

/*
* C - 2x2 Placing
* https://atcoder.jp/contests/abc436/tasks/abc436_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.HashSet;
import java.util.Scanner;

class TilePos {
	int r;
	int c;

	TilePos(int r, int c) {
		this.r = r;
		this.c = c;
	}

	public String toString() {
		return "(" + r + "," + c + ")";
	}

	@Override
	public boolean equals(Object obj) { // Objectである必要がある。
		return (this.r == ((TilePos) obj).r) && (this.c == ((TilePos) obj).c);
	}

	@Override
	public int hashCode() {
		return ("" + this.r + "_" + this.c).hashCode();
	}
}

public class C {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 辺の長さ
		int M = sc.nextInt(); // ブロックの数

		HashSet<TilePos> map = new HashSet<>();
		for (int i = 0; i < M; i++) {
			int R = sc.nextInt();
			int C = sc.nextInt();

			boolean overlap = false;
			for (int r = -1; r <= 1; r++) {
				for (int c = -1; c <= 1; c++) {
//					System.out.println("Check: r:" + (R + r) + ", c: " + (C + c));
					if (map.contains(new TilePos(R + r, C + c))) {
						overlap = true;
//						System.out.println("Overlap: r:" + (R + r) + ", c: " + (C + c));
					}
				}
			}
			if (!overlap)
				map.add(new TilePos(R, C));
//			System.out.println(map);
		}

		sc.close();

		System.out.println(map.size());
	}

}
