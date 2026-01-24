package abc432;

/*
* C - Candy Tribulation
* https://atcoder.jp/contests/abc432/tasks/abc432_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/
import java.util.Scanner;

public class C {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 重さは、32ビットに収まらないことがある。

        int N = sc.nextInt(); // 人数
        long X = sc.nextLong(); // Xの重さ
        long Y = sc.nextLong(); // Yの重さ
        long delta_candy = Y - X; // 飴の重さの差

        long[] candys = new long[N]; // 配る飴の数
        // 全部大きな飴と、全部小さな飴の両方から攻める。
        long[] num_Y = new long[N]; // 大きな飴の数
        long[] weight_Y = new long[N]; // もらえる飴の重さ
        long[] num_X = new long[N]; // 小さな飴の数
        long[] weight_X = new long[N]; // もらえる飴の重さ
        long total_candys = 0;
        for (int i = 0; i < N; i++) {
            candys[i] = Long.parseLong(sc.next()); // もらえる飴の数。
            // とりあえず全て大きな飴にする。
            num_Y[i] = candys[i];
            weight_Y[i] = num_Y[i] * Y;
            // 全部が小さい飴の場合
            num_X[i] = candys[i];
            weight_X[i] = num_X[i] * X;
            total_candys += candys[i];
        }

        sc.close(); // 使ったら閉じる。

        // デバッグ
        // for (int i = 0; i < N; i++) {
        // System.out.printf("合計数: %3d, 大きな飴の数: %3d, 重さ: %3d%n", candys[i], num_Y[i],
        // weight_Y[i]);
        // }

        // 最小の重さを探す。便利なメソッドがないので自力で探す。
        // 最小を探しておかないと、繰返しが無駄に多くなる。
        long min_weight_Y = weight_Y[0];
        long max_weight_X = weight_X[0];
        for (int i = 1; i < N; i++) {
            if (weight_Y[i] < min_weight_Y) {
                min_weight_Y = weight_Y[i];
            }
            if (weight_X[i] > max_weight_X) {
                max_weight_X = weight_X[i];
            }
        }

        long replace_num; // 小さい飴に置き換える数
        // 飴の重さが均一になった
        boolean balanced_Y;
        do {
            balanced_Y = true;
            int last_updated_Y_at = N - 1;
            for (int i = 0; i < N; i++) {
                // 全部大きい方から更新
                if (weight_Y[i] > min_weight_Y) {
                    // 小さい飴で置き換えて、最小の重さより小さくする。
                    replace_num = (weight_Y[i] - min_weight_Y) / delta_candy;

                    num_Y[i] -= replace_num; // 置き換えた時の大きな飴の数
                    // 重さを更新
                    // weight_Y[i] = num_Y[i] * Y + (candys[i] - num_Y[i]) * X;
                    weight_Y[i] -= delta_candy * replace_num;
                    // 最小よりも重かったらもう1個置き換える。
                    if (weight_Y[i] > min_weight_Y) {
                        num_Y[i] -= 1;
                        weight_Y[i] -= delta_candy;
                    }

                    if (num_Y[i] < 0) {
                        // 個数が負はありえない、すなわち条件を満たせない。
                        // 0個、全部小さい飴はOK
                        System.out.println(-1);
                        return;
                    }
                }

                // 更新を含めて重さが最小より小さいかか確認
                if (weight_Y[i] < min_weight_Y) {
                    // より軽い人が見つかったので、最小を更新
                    min_weight_Y = weight_Y[i];

                    balanced_Y = false; // 最小値が変わった
                    last_updated_Y_at = i;
                } else if ((i == last_updated_Y_at) && balanced_Y) {
                    // 一周してバランスしていたら終了
                    break;
                }

                // 全部小さい方から更新
                // 小さい方から更新すると、大きい飴の最大数にならない。これをリミットにすることで早期終了になる。
                if (weight_X[i] < max_weight_X) {
                    // 大きい飴で置き換えて、最大の重さより大きくする。
                    replace_num = (max_weight_X - weight_X[i]) / delta_candy;

                    num_X[i] -= replace_num; // 置き換えた時の小さな飴の数
                    // 重さを更新
                    weight_X[i] += delta_candy * replace_num;
                    // 最小よりも重かったらもう1個置き換える。
                    if (weight_X[i] < max_weight_X) {
                        num_X[i] -= 1;
                        weight_X[i] += delta_candy;
                    }

                    if (num_X[i] < 0) {
                        // 個数が負はありえない、すなわち条件を満たせない。
                        System.out.println(-1);
                        return;
                    }
                }

                // 更新を含めて重さが最小より小さいかか確認
                if (weight_X[i] > max_weight_X) {
                    // より軽い人が見つかったので、最小を更新
                    max_weight_X = weight_X[i];
                }

                if (num_Y[i] < (candys[i] - num_X[i])) {
                    System.out.println(-1);
                    return;
                }
            }
        } while (!balanced_Y); // 均一になるまで繰り返し

        // 飴の重さを揃えられた。大きな飴の「合計数」を探す。
        // 変数を定義しないで頭に加算する。
        for (int i = 1; i < N; i++) {
            num_Y[0] += num_Y[i];
        }
        System.out.println(num_Y[0]);
    }

}
