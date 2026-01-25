package abc433;

/*
* C - 1122 Substring 2
* https://atcoder.jp/contests/abc433/tasks/abc433_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.ArrayList;
import java.util.Scanner;

class Item {
	char c;
	int count = 1;
	int c_num;

	Item(char c) {
		this.c = c;
		//this.c_num = Integer.parseInt(c);
		this.c_num = c - '0'; // 文字コードの並びで数値にする。
	}

	void add() {
		count++;
	}
}

public class C {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String S = sc.next(); // 入力文字列

		sc.close();

		//System.out.println(S);

		ArrayList<Item> items = new ArrayList<Item>();

		items.add(new Item(S.charAt(0)));
		char c;
		int items_index = 0;
		for (int i = 1; i < S.length(); i++) {
			c = S.charAt(i);

			if (items.get(items_index).c == c) {
				items.get(items_index).add();
			} else {
				items_index++;
				items.add(new Item(c));
			}

		}

		// debug
//		for (Item item : items) {
//			System.out.println(item.c + "(" + item.c_num + "): " + item.count);
//		}

		int count = 0;
		for (int i = 0; i < (items.size() - 1); i++) {
			if ((items.get(i).c_num + 1) == items.get(i + 1).c_num) {
				count += Math.min(items.get(i).count, items.get(i + 1).count);
			}
		}
		System.out.println(count);
	}

}
