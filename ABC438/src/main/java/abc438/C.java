package abc438;

import java.util.ArrayList;

/*
* C - 1D puyopuyo
* https://atcoder.jp/contests/abc438/tasks/abc438_c
*
* Test command: gradle test --tests CTest
*/

import java.util.Scanner;

public class C {

    static class Item {
        int key;
        int count;

        Item(int key) {
            this.key = key;
            this.count = 1;
        }

        public String toString() {
            return "(" + key + "=>" + count + ") ";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // Aの数
        int count = N;
        ArrayList<Item> A = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int tmp = sc.nextInt();
            if (A.size() == 0) {
                A.add(new Item(tmp));
            } else if (A.getLast().key == tmp) {
                A.getLast().count += 1;
                if (A.getLast().count == 4) {
                    A.removeLast();
                    count -= 4;
                }
            } else {
                A.add(new Item(tmp));
            }
        }

        sc.close();

        System.out.println(count);
    }
}
