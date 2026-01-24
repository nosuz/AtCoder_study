package abc431;

/*
* C - Robot Factory
* https://atcoder.jp/contests/abc431/tasks/abc431_c
*
* Test command: gradle test --tests CTest
* Test command: gradle test --tests CTest.sample1
*/

import java.util.Arrays;
import java.util.Scanner;

class Part implements Comparable<Part> {
    int weight;
    boolean is_head;

    Part(int weight, boolean is_head) {
        this.weight = weight;
        this.is_head = is_head;
    }

    static void sort(Part[] parts) {
        Part tmpPart;
        for (int i = 0; i < (parts.length - 1); i++) {
            for (int j = (i + 1); j < parts.length; j++) {
                if (parts[i].weight > parts[j].weight) {
                    tmpPart = parts[i];
                    parts[i] = parts[j];
                    parts[j] = tmpPart;
                } else if ((parts[i].weight == parts[j].weight) && !parts[i].is_head && parts[j].is_head) {
                    tmpPart = parts[i];
                    parts[i] = parts[j];
                    parts[j] = tmpPart;
                }
            }
        }
    }

    static void printParts(Part[] parts) {
        for (int i = 0; i < parts.length; i++) {
            System.out.printf("%5d ", parts[i].weight);
        }
        System.out.println();
        for (int i = 0; i < parts.length; i++) {
            System.out.printf("%5b ", parts[i].is_head);
        }
        System.out.println();
    }

    public int compareTo(Part other) {
        if (this.weight > other.weight) {
            return 1;
        } else if (this.weight == other.weight) {
            if ((!this.is_head) && other.is_head) {
                return 1;
            } else if (this.is_head && (!other.is_head)) {
                return -1;
            } else {
                return 0;
            }
        } else {
            return -1;
        }
    }

    public int getWeight() {
        return this.weight;
    }
}

public class C {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt(); // 頭のパーツ数
        int N = sc.nextInt(); // 体のパーツ数
        int K = sc.nextInt(); // 作成したいロボットの数

        Part[] parts = new Part[M + N];
        for (int i = 0; i < M; i++) {
            parts[i] = new Part(sc.nextInt(), true);
        }
        for (int i = 0; i < N; i++) {
            parts[M + i] = new Part(sc.nextInt(), false);
        }

        sc.close();

        Arrays.sort(parts);

        int balance = 0; // headとbodyの差
        int balanceMemo[] = new int[parts.length];
        int bodyCount = 0;
        for (int j = (parts.length - 1); j >= 0; j--) {
            if (parts[j].is_head) {
                balance -= 1;
                if (balance >= 0) {
                    bodyCount += 1;
                    if (bodyCount >= K) {
                        System.out.println("Yes");
                        return;
                    }
                }
            } else {
                if (balance < 0) {
                    // 過剰の頭は無視する
                    balance = 1;
                } else {
                    balance += 1;
                }
            }
            balanceMemo[j] = balance;
        }
        System.out.println("No");
    }

}
