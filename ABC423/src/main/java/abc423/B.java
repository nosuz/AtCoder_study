package abc423;

import java.util.Arrays;

/*
* B - Locked Rooms
* https://atcoder.jp/contests/abc423/tasks/abc423_b
*
* Test command: gradle test --tests BTest
* Test command: gradle test --tests BTest.sample1
*/

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 部屋の数
        int L[] = new int[N];
        for (int i = 0; i < N; i++) {
            int l = sc.nextInt(); // 鍵の状態, 0: open, 1: closed
            L[i] = l;
        }

        sc.close();

        boolean room[] = new boolean[N + 1];
        room[0] = true;
        for (int i = 0; i < N; i++) {
            if (L[i] == 1) {
                // closed
                break;
            } else if (room[i + 1]) {
                break;
            } else {
                room[i + 1] = true;
            }
        }

        room[N] = true;
        for (int i = (N - 1); i >= 0; i--) {
            if (L[i] == 1) {
                // closed
                break;
            } else if (room[i]) {
                break;
            } else {
                room[i] = true;
            }
        }
        // System.out.println(Arrays.toString(room));
        int ans = 0;
        for (int i = 0; i < N; i++) {
            if (!room[i])
                ans++;
        }
        System.out.println(ans);
    }
}
