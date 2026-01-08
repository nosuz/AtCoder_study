package abc439;

/*
* D - Kadomatsu Subsequence
* https://atcoder.jp/contests/abc439/tasks/abc439_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class D {
    static class Item {
        ArrayList<Integer> i = new ArrayList<>();
        ArrayList<Integer> j = new ArrayList<>();
        ArrayList<Integer> k = new ArrayList<>();

        boolean isOk() {
            return ((j.size() > 0) && (i.size() > 0) && (k.size() > 0)) ? true : false;
        }

        public String toString() {
            return i.toString() + "," + j.toString() + "," + k.toString();
        }
    }

    static class MinMax {
        int min;
        int max;

        MinMax(int min, int max) {
            this.min = min;
            this.max = max;
        }

        public String toString() {
            return "Min: " + min + ", Max: " + max;
        }
    }

    static MinMax binSearch(int target, ArrayList<Integer> list) {
        // System.out.println(target + ", " + list);

        int min;
        int max;

        int low = 0;
        int hi = list.size() - 1;
        int p = 0;

        while (hi >= low) {
            p = (hi + low) / 2;
            // System.out.println("hi: " + hi + ", p: " + p + ", low: " + low);
            if (target < list.get(p)) {
                hi = p - 1;
            } else if (target > list.get(p)) {
                low = p + 1;
            }
            // System.out.println("updated hi: " + hi + ", p: " + p + ", low: " + low);
        }
        min = low;
        max = list.size() - low;

        return new MinMax(min, max);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        long A[] = new long[N];
        HashMap<Long, Item> indexes = new HashMap<>();
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();

            long val;
            Item item;
            val = A[i] * 21;
            if (val % 105 == 0) {
                if (!indexes.containsKey(val))
                    indexes.put(val, new Item());
                item = indexes.get(val);
                item.j.add(i);
            }

            val = A[i] * 15;
            if (val % 105 == 0) {
                if (!indexes.containsKey(val))
                    indexes.put(val, new Item());
                item = indexes.get(val);
                item.i.add(i);
            }

            val = A[i] * 35;
            if (val % 105 == 0) {
                if (!indexes.containsKey(val))
                    indexes.put(val, new Item());
                item = indexes.get(val);
                item.k.add(i);
            }
        }
        sc.close();
        // System.out.println(indexes);

        long result = 0;
        for (Item item : indexes.values()) {
            // System.out.println(item);
            if (item.isOk()) {
                for (int j_idx = 0; j_idx < item.j.size(); j_idx++) {
                    int j_val = item.j.get(j_idx);

                    MinMax minmax;
                    minmax = binSearch(j_val, item.i);
                    // System.out.println("Max: " + minmax.max + ", Min: " + minmax.min);
                    int i_max = minmax.max;
                    int i_min = minmax.min;

                    minmax = binSearch(j_val, item.k);
                    // System.out.println("Max: " + minmax.max + ", Min: " + minmax.min);
                    int k_max = minmax.max;
                    int k_min = minmax.min;

                    // System.out.println("Max i: " + i_max + ", k: " + k_max + "| Min i: " + i_min
                    // + ", k: " + k_min);
                    result += (long) i_max * (long) k_max + (long) i_min * (long) k_min;
                }
            }
        }

        System.out.println(result);
    }

}
