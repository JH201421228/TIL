package boj_2243;

import java.io.*;
import java.util.*;

public class Main {

    public static long[] tree = new long[4000004];

    public static int S(int s, int e, long v, int tree_idx) {
        if (s == e) {
            return s;
        }

        int mid = (s+e) / 2;
        if (tree[tree_idx*2] >= v) {
            return S(s, mid, v, tree_idx*2);
        }
        else {
            return S(mid+1, e, v-tree[tree_idx*2], tree_idx*2+1);
        }
    }

    public static void U(int s, int e, int idx, long c, int tree_idx) {
        if (idx > e || idx < s) {
            return;
        }

        tree[tree_idx] += c;

        if (s == e) {
            return;
        }

        int mid = (s+e) / 2;
        U(s, mid, idx, c, tree_idx*2);
        U(mid+1, e, idx, c, tree_idx*2+1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            if (a == 1) {
                long b = Long.parseLong(input[1]);
                int ans = S(1, 1000001, b, 1);
                System.out.println(ans);
                U(1, 1000001, ans, -1, 1);
            }
            else {
                int b = Integer.parseInt(input[1]);
                long c = Long.parseLong(input[2]);
                U(1, 1000001, b, c, 1);
            }
        }
    }
}