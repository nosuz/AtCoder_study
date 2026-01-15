package abc440;

/*
* D - Forbidden List 2
* https://atcoder.jp/contests/abc440/tasks/abc440_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class D {

    static class Item {
        int begin;
        int end;
        int spaces;

        Item() {
            this.begin = 0;
            this.end = 0;
            this.spaces = 0;
        }

        Item(int begin, int end, int spaces) {
            this.begin = begin;
            this.end = end;
            this.spaces = spaces;
        }

        public String toString() {
            return "(begin:" + begin + ", end:" + end + ", spaces:" + spaces + ")";
        }
    }

    static int binSearchX(int target, ArrayList<Item> list) {
        // System.out.println("target:" + target);
        // https://stackoverflow.com/a/70044648 を使うとうまくいきそう

        int low = 0;
        int hi = list.size() - 1;
        int p;
        int result = -1;

        while (hi >= low) {
            p = (hi + low) / 2;
            // System.out.println("hi: " + hi + ", p: " + p + ", low: " + low);
            if (target < list.get(p).begin) {
                hi = p - 1;
            } else if (target > list.get(p).end) {
                result = p;
                low = p + 1;
            } else {
                return p;
            }
            // System.out.println("updated hi: " + hi + ", p: " + p + ", low: " + low);
        }

        // true point is less than this
        return result;
    }

    static int binSearchY(int target, ArrayList<Item> list, int low) {
        // System.out.println(target);
        // https://stackoverflow.com/a/70044648 を使うとうまくいきそう

        // int low = 0;
        int hi = list.size() - 1;
        int p;
        int result = -1;

        while (hi >= low) {
            p = (hi + low) / 2;
            // System.out.println("hi: " + hi + ", p: " + p + ", low: " + low);
            if (target < list.get(p).spaces) {
                hi = p - 1;
            } else if (target > list.get(p).spaces) {
                result = p;
                low = p + 1;
            } else {
                return p;
            }
            // System.out.println("updated hi: " + hi + ", p: " + p + ", low: " + low);
        }

        // true point is less than this
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int Q = sc.nextInt();

        int A[] = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);
        // System.out.println(Arrays.toString(A));

        ArrayList<Item> a = new ArrayList<>();
        a.add(new Item());
        for (int i = 0; i < N; i++) {
            Item last = a.get(a.size() - 1);
            if ((A[i] - last.end) == 1) {
                // continue
                last.end = A[i];
            } else {
                a.add(new Item(A[i], A[i], last.spaces + A[i] - last.end - 1));
            }
        }
        // System.out.println(a);

        for (int i = 0; i < Q; i++) {
            int X = sc.nextInt();
            int Y = sc.nextInt();

            int xi = binSearchX(X, a);
            // System.out.println("xi:" + xi);
            Item itemX = a.get(xi);
            int req_spaces;
            if ((itemX.begin <= X) && (X <= itemX.end)) {
                // on the item
                req_spaces = Y;
            } else {
                req_spaces = (X - itemX.end - 1) + Y;
            }
            req_spaces += itemX.spaces;
            // System.out.println("spaces:" + req_spaces);

            int yi = binSearchY(req_spaces, a, xi);
            // System.out.println("yi:" + yi);
            Item itemY = a.get(yi);

            // System.out.println("req:" + req_spaces + " have:" + itemY);
            int result;
            if (req_spaces == itemY.spaces) {
                result = itemY.begin - 1;
            } else {
                result = req_spaces - itemY.spaces + itemY.end;
            }
            System.out.println(result);
        }

        sc.close();
    }

}
