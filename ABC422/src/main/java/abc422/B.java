package abc422;

/*
* B - Looped Rope
* https://atcoder.jp/contests/abc422/tasks/abc422_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int H = con.nextInt();
        int W = con.nextInt();

        String S[] = new String[H];
        for (int h = 0; h < H; h++) {
            S[h] = con.next();
        }
        con.close();
        // for (var s : S) {
        // System.out.println(s);
        // }

        int[][] count = new int[H][W];
        // 隣の#を数える
        for (int h = 0; h < H; h++) {
            for (int w = 0; w < W; w++) {
                // 左を確認
                if ((w > 0) && (S[h].charAt(w - 1) == '#'))
                    count[h][w] += 1;

                // 右を確認
                if ((w < (W - 1)) && (S[h].charAt(w + 1) == '#'))
                    count[h][w] += 1;

                // 上を確認
                if ((h > 0) && (S[h - 1].charAt(w) == '#'))
                    count[h][w] += 1;

                // 下を確認
                if ((h < (H - 1)) && (S[h + 1].charAt(w) == '#'))
                    count[h][w] += 1;
            }
        }
        // for (var c : count) {
        // System.out.println(Arrays.toString(c));
        // }

        boolean result = true;
        failed: for (int h = 0; h < H; h++) {
            for (int w = 0; w < W; w++) {
                if (S[h].charAt(w) == '#') {
                    if ((count[h][w] == 0) || (count[h][w] % 2 != 0)) {
                        result = false;
                        break failed;
                    }
                }
            }
        }

        System.out.println(result ? "Yes" : "No");
    }

}
