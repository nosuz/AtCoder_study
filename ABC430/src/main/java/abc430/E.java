package abc430;

/*
* E - Shift String
* https://atcoder.jp/contests/abc430/tasks/abc430_e
*
* Test command: gradle test --tests ETest
* Test command: gradle test --tests ETest.sample1
*/

import java.util.Arrays;
import java.util.Scanner;

/*
1
1010001
1000110

1
100001101110000001010110110001
101100011000011011100000010101

1
000000000000000111111111111111
000000000000001111111111111110

1
010110010001001110111110100011111101111000100111011111011010010000010110101001100000011101000101001110110000011000011001010010111111011111100001100001000001010100101100101101110010001111010011011110111111011011110100000011101110011111111010011111011110101010000000101101110100100100011110010010000110011110101110101001110011101110011110101100101
111001111010110010101011001000100111011111010001111110111100010011101111101101001000001011010100110000001110100010100111011000001100001100101001011111101111110000110000100000101010010110010110111001000111101001101111011111101101111010000001110111001111111101001111101111010101000000010110111010010010001111001001000011001111010111010100111001110

expected: 326

1
01010
01010

 */

public class E {
    static final int P = 31; // 31, 53, 257 適当な素数
    static final int M = 1_000_000_007; // 10^9 + 7 大きな素数

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int T = con.nextInt();
        for (int t = 0; t < T; t++) {
            String A = con.next();
            String B = con.next();

            // 固定トークンではなく、全体をハッシュする
            // substringは、新しいStringを作るのでダメ
            // ローリングハッシュを使う。
            final int len = A.length();

            long pow[] = new long[len];
            for (int i = 0; i < len; i++) {
                if (i == 0) {
                    pow[0] = P;
                } else {
                    pow[i] = (pow[i - 1] * P) % M;
                }
            }
            // System.out.println(Arrays.toString(pow));

            // Bのハッシュを計算する。
            long b_hash = 0;
            for (int i = 0; i < len; i++) {
                b_hash += (long) B.charAt(i) * pow[len - i - 1];
                b_hash %= M;
            }
            // System.out.println(b_hash);

            // マッチする部分を探す。
            int ans = -1;
            long hash = 0;
            for (int i = 0; i < len; i++) {
                if (i == 0) {
                    hash = (long) A.charAt(i) * pow[len - 1];
                } else {
                    hash += (long) A.charAt(i) * pow[len - i - 1];
                }
                hash = (hash % M + M) % M; // 負になることをガード
            }
            if (hash == b_hash) {
                ans = 0;
            } else {
                for (int i = 1; i < len; i++) {
                    // 左端の寄与をキャンセル
                    hash -= (long) A.charAt(i - 1) * pow[len - 1];
                    // 右端に追加
                    hash += (long) A.charAt((i + len - 1) % len);
                    hash *= P;
                    hash = (hash % M + M) % M; // 負になることをガード
                    // System.out.println(hash);

                    if (hash == b_hash) {
                        ans = i;
                        break;
                    }
                }
            }
            System.out.println(ans);
        }

        con.close();

    }

}
