package abc436;

/*
* D - Teleport Maze
* https://atcoder.jp/contests/abc436/tasks/abc436_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;

// ABC436 D - Teleport Maze
// https://atcoder.jp/contests/abc436/tasks/abc436_d

class Pos {
	int r;
	int c;
	int step;

	Pos(int r, int c, int step) {
		this.r = r;
		this.c = c;
		this.step = step + 1;
	}

	Pos(int r, int c) {
		this.r = r;
		this.c = c;
		this.step = 0;
	}

	void setStep(int step) {
		this.step = step + 1;
	}

	public String toString() {
		return "(" + r + "," + c + "){" + step + "}";
	}
}

public class D {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int H = sc.nextInt(); // 迷路のrow数
		int W = sc.nextInt(); // 迷路のcolumn数

		HashMap<Character, ArrayList<Pos>> warp = new HashMap<>();
		char map[][] = new char[H][W];
		for (int r = 0; r < H; r++) {
			map[r] = sc.next().toCharArray();
			for (int c = 0; c < W; c++) {
				if (map[r][c] != '.' && map[r][c] != '#') {
//					System.out.println("Warp: " + map[r][c]);
					if (warp.get(map[r][c]) == null)
						warp.put(map[r][c], new ArrayList<Pos>());
					warp.get(map[r][c]).add(new Pos(r, c));
				}
			}
		}

		sc.close();

		// ゴールから逆向きに探索。最小を求めるので幅優先で探索。queueを使う。
		// ワープポイントはつながっているところを全てターゲットに加える。

		// ゴールとスタートが障害物ではないことを確認する
		if (map[H - 1][W - 1] == '#') {
			System.out.println("-1");
		} else {
			LinkedList<Pos> que = new LinkedList<>();
			que.add(new Pos(0, 0));
			while (que.size() > 0) {
//				System.out.println(que);
				Pos pos = que.remove();
				if ((pos.r == (H - 1)) && (pos.c == (W - 1))) {
//					System.out.println("Yes");
					System.out.println(pos.step);
					return;
				}
				switch (map[pos.r][pos.c]) {
				case '*':
					// visited
					break;
				case '#':
					// 障害物
					break;
				case '.':
//					System.out.println(pos.r + "," + pos.c + "[" + pos.step + "]");
					map[pos.r][pos.c] = '*';
					// 範囲外を除く必要がある。
					if (pos.r != 0) {
						que.add(new Pos(pos.r - 1, pos.c, pos.step));
					}
					if (pos.r != (H - 1)) {
						que.add(new Pos(pos.r + 1, pos.c, pos.step));
					}
					if (pos.c != 0) {
						que.add(new Pos(pos.r, pos.c - 1, pos.step));
					}
					if (pos.c != (W - 1)) {
						que.add(new Pos(pos.r, pos.c + 1, pos.step));
					}
					break;
				default:
					// ワープポイント
//					System.out.println(pos.r + "," + pos.c + "[" + pos.step + "]");
					if (warp.containsKey(map[pos.r][pos.c])) {
//					ArrayList<Pos> w = warp.get(map[pos.r][pos.c]);
						ArrayList<Pos> w = warp.remove(map[pos.r][pos.c]);
						for (int i = 0; i < w.size(); i++) {
							Pos jump = w.get(i);
							jump.setStep(pos.step);
//						System.out.println("Add: " + jump);
							que.add(jump);
						}
					}
//					for (Pos w : warp.get(map[pos.r][pos.c])) {
//						System.out.println("Add: " + pos);
//						que.add(w);
//					}
					map[pos.r][pos.c] = '*';
					if (pos.r != 0) {
						que.add(new Pos(pos.r - 1, pos.c, pos.step));
					}
					if (pos.r != (H - 1)) {
						que.add(new Pos(pos.r + 1, pos.c, pos.step));
					}
					if (pos.c != 0) {
						que.add(new Pos(pos.r, pos.c - 1, pos.step));
					}
					if (pos.c != (W - 1)) {
						que.add(new Pos(pos.r, pos.c + 1, pos.step));
					}
				}
			}
			System.out.println("-1");
		}
	}
}
