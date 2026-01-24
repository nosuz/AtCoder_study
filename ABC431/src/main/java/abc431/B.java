package abc431;

/*
* B - Robot Weight
* https://atcoder.jp/contests/abc431/tasks/abc431_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

/*
31 //最初の重さ
4 //item数
15 92 65 35 // items
4 // query数
3
1
4
1

 */

import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int weight = con.nextInt();
        int num_items = con.nextInt();

        int[] items = new int[num_items];
        boolean[] wear = new boolean[num_items]; // init False
        for (int i = 0; i < num_items; i++) {
            items[i] = con.nextInt();
        }

        int num_query = con.nextInt();
        for (int i = 0; i < num_query; i++) {
            int item = con.nextInt() - 1;
            if (wear[item]) {
                // 装着済み
                weight -= items[item];
            } else {
                // 未装着
                weight += items[item];
            }
            wear[item] = !wear[item]; // toggle 装着状態
            System.out.println(weight);
        }
        // System.out.println(H + "-" + B);
        // String line = con.nextLine();
        con.close(); // 使ったら閉じる

    }

}
