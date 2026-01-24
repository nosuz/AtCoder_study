package abc430;

/*
* B - Count Subgrid
* https://atcoder.jp/contests/abc430/tasks/abc430_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.HashSet;
import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int N = con.nextInt();
        int M = con.nextInt();
        // System.out.println(N + "x" + M);

        String[] grid = new String[N];
        for (int i = 0; i < N; i++) {
            grid[i] = con.next(); // nextLine()はダメ。なぜ？
        }
        con.close();

        // 文字列にして、同じかどうか調べる。Set()がある？
        // NとM共に10以下なので、全ての組み合わせを配列に入れてもOKでないかな。
        HashSet<String> list = new HashSet<>();

        for (int y = 0; y <= N - M; y++) {
            for (int x = 0; x <= N - M; x++) {
                // gridから文字列を切り出す。
                String tmp = "";
                for (int delta = 0; delta < M; delta++) {
                    tmp += grid[y + delta].substring(x, x + M);
                }
                // System.out.println("tmp: " + tmp);
                list.add(tmp);
            }
        }

        // System.out.println(list.length);
        System.out.println(list.size());

    }

}
