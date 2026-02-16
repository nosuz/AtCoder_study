package abc430;

/*
* D - Neighbor Distance
* https://atcoder.jp/contests/abc430/tasks/abc430_d
*
* Test command: gradle test --tests DTest
* Test command: gradle test --tests DTest.sample1
*/

import java.util.Scanner;
import java.util.Arrays;

/*
 * 5
 * 5 2 7 4 108728325
 *
 */
public class D {

    static class Person implements Comparable {
        int pos;
        int left = 0;
        int right = 0;
        int dist = 0;

        Person(int pos) {
            this.pos = pos;
        }

        public int compareTo(Person other) {
            return Integer.compare(this.pos, other.pos);
        }

        @Override
        public int compareTo(Object o) {
            return Integer.compare(this.pos, ((Person) o).pos);
        }

        @Override
        public String toString() {
            return "[pos=" + pos + ", left=" + left + ", right=" + right + ", dist=" + dist + "]";
        }
    }

    static int binSearch(int target, Person[] list) {
        int left = 0;
        int right = list.length - 1;
        int p = -1;

        while (right >= left) {
            p = (right + left) / 2;
            if (target < list[p].pos) {
                right = p - 1;
            } else if (target > list[p].pos) {
                left = p + 1;
            } else {
                return p;
            }
        }

        return p;
    }

    public static void main(String[] args) {
        Scanner con = new Scanner(System.in);

        int N = con.nextInt();

        Person list[] = new Person[N + 1];
        int order[] = new int[N + 1];
        list[0] = new Person(0);
        order[0] = 0;

        for (int x = 1; x <= N; x++) {
            int pos = con.nextInt();
            list[x] = new Person(pos);
            order[x] = pos;
        }

        con.close();

        Arrays.sort(list);
        // System.out.println(Arrays.toString(list));

        long total_dist = 0;
        for (int x = 0; x <= N; x++) {
            Person p = list[x];
            p.left = x - 1;
            p.right = x + 1;

            if (x == 0) {
                p.dist = list[1].pos - p.pos;
            } else if (x == N) {
                p.dist = p.pos - list[N - 1].pos;
                p.right = -1; // no right
            } else {
                int left_dist = p.pos - list[x - 1].pos;
                int right_dist = list[x + 1].pos - p.pos;
                p.dist = Math.min(left_dist, right_dist);
            }
            total_dist += p.dist;
            // System.out.println(Arrays.toString(list));
        }
        // System.out.println(Arrays.toString(list));
        // System.out.println(total_dist);

        long result[] = new long[N + 1];
        result[N] = total_dist;
        for (int i = N; i > 0; i--) {
            int pos = binSearch(order[i], list);

            Person me = list[pos];
            total_dist -= me.dist;
            Person left = list[me.left];
            if (me.right == -1) {
                // right end
                left.right = -1;
                total_dist -= left.dist;
                if (left.pos != 0) {
                    left.dist = left.pos - list[left.left].pos;
                    total_dist += left.dist;
                }
            } else {
                Person right = list[me.right];
                int dist = right.pos - left.pos;
                // 左隣を更新
                left.right = me.right;
                total_dist -= left.dist;
                if (left.left == -1) {
                    left.dist = dist;
                } else {
                    left.dist = Math.min(dist, left.pos - list[left.left].pos);
                }
                total_dist += left.dist;

                // 右隣を更新
                right.left = me.left;
                total_dist -= right.dist;
                if (right.right == -1) {
                    right.dist = dist;
                } else {
                    right.dist = Math.min(dist, list[right.right].pos - right.pos);
                }
                total_dist += right.dist;
            }
            result[i - 1] = total_dist;
            // System.out.println(Arrays.toString(list));
        }
        // System.out.println(Arrays.toString(result));
        for (int i = 1; i <= N; i++) {
            System.out.println(result[i]);
        }
    }

}
