package abc443;

/*
* D - Pawn Line
* https://atcoder.jp/contests/abc443/tasks/abc443_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

/*
1
5
5 2 1 3 4

1
3
1 3 1

1
20
7 4 6 2 15 5 17 15 1 8 18 1 5 1 12 11 2 7 8 14

*/

public class D {

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int T = con.nextInt();
        for (int t = 0; t < T; t++) {
            HashMap<Integer, ArrayList<Integer>> pos = new HashMap<>();

            int N = con.nextInt();
            int R[] = new int[N];
            int max_n = 0;
            for (int n = 0; n < N; n++) {
                R[n] = con.nextInt();
                max_n = Math.max(max_n, R[n]);
                if (!pos.containsKey(R[n]))
                    pos.put(R[n], new ArrayList<Integer>());
                pos.get(R[n]).add(n);
            }
            // System.out.println(Arrays.toString(R));
            // System.out.println(levels);
            // System.out.println(pos);

            long steps = 0;
            boolean fixed[] = new boolean[N];
            ArrayList<Integer> left_que = new ArrayList<>();
            ArrayList<Integer> right_que = new ArrayList<>();
            ArrayList<Integer> next_left_que = new ArrayList<>();
            ArrayList<Integer> next_right_que = new ArrayList<>();
            for (int level = 1; level < max_n; level++) {
                // Key Point
                // 新しくオブジェクトを作らないとLTEになる
                // System.out.println("level:" + level);
                // if (pos.containsKey(level)) {
                // left_que = pos.get(level);
                // right_que = pos.get(level);
                // }
                if (pos.containsKey(level)) {
                    left_que = new ArrayList<>(pos.get(level));
                    right_que = new ArrayList<>(pos.get(level));
                } else {
                    left_que = new ArrayList<>();
                    right_que = new ArrayList<>();
                }

                if (next_left_que.size() > 0)
                    left_que.addAll(next_left_que);
                if (next_right_que.size() > 0)
                    right_que.addAll(next_right_que);
                next_left_que = new ArrayList<>();
                next_right_que = new ArrayList<>();

                for (var l : left_que) {
                    // System.out.println("L: R[" + l + "]:" + fixed[l]);
                    if ((l <= 0) || (fixed[l - 1]))
                        continue;

                    fixed[l] = true;
                    int delta = R[l - 1] - R[l];
                    // System.out.println("L: R[" + (l - 1) + "]:" + R[l - 1] + "->" + (R[l] + 1) +
                    // "step:" + (delta - 1));
                    if (delta > 1) {
                        // 一つ下に移動させる。
                        steps += delta - 1;
                        R[l - 1] = R[l] + 1;
                        fixed[l - 1] = true;
                    }
                    next_left_que.add(l - 1);
                }

                for (var r : right_que) {
                    // System.out.println("R: R[" + r + "]:" + fixed[r]);
                    if ((r >= (N - 1)) || (fixed[r + 1]))
                        continue;

                    fixed[r] = true;
                    int delta = R[r + 1] - R[r];
                    // System.out.println("R: R[" + (r + 1) + "]:" + R[r + 1] + "->" + (R[r] + 1) +
                    // "step:" + (delta - 1));
                    if (delta > 1) {
                        // 一つ下に移動させる。
                        steps += delta - 1;
                        R[r + 1] = R[r] + 1;
                        fixed[r + 1] = true;
                    }
                    next_right_que.add(r + 1);
                }

            }

            // System.out.println(Arrays.toString(R));
            System.out.println(steps);

        }

        con.close();

    }

}
