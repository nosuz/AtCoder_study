package abc441;

/*
* D - Paid Walk
* https://atcoder.jp/contests/abc441/tasks/abc441_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class D {

    static int S;
    static int T;
    static Next[] next;
    static TreeSet<Integer> result = new TreeSet<>();

    static class Path {
        int node;
        int cost;

        Path(int next_node, int cost) {
            this.node = next_node;
            this.cost = cost;
        }

        @Override
        public String toString() {
            return "(" + node + ", " + cost + ")";
        }
    }

    static class Next {
        ArrayList<Path> path = new ArrayList<>();

        void add(int node, int cost) {
            path.add(new Path(node, cost));
        }

        @Override
        public String toString() {
            return path.toString();
        }
    }

    static void walk(int node, int l, int cost) {
        if (l == 0) {
            if ((cost >= S) && (cost <= T)) {
                result.add(node);
            }
        } else {
            for (Path path : next[node].path) {
                // System.out.println(path);
                walk(path.node, l - 1, cost + path.cost);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int L = sc.nextInt();
        S = sc.nextInt();
        T = sc.nextInt();

        next = new Next[N + 1];
        for (int i = 0; i <= N; i++)
            next[i] = new Next();

        for (int i = 0; i < M; i++) {
            int U = sc.nextInt();
            int V = sc.nextInt();
            int C = sc.nextInt();

            next[U].add(V, C);
        }

        sc.close();
        // System.out.println(Arrays.toString(next));

        for (Path path : next[1].path) {
            walk(path.node, L - 1, path.cost);
        }

        // System.out.println(result);
        if (result.size() == 0) {
            System.out.println();
        } else {
            for (int node : result) {
                System.out.println(node);
            }
        }

    }

}
