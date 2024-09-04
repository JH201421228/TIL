package boj_1395;

import java.util.*;
import java.io.*;

public class Main {
    static int[] fake;
    static int[] tree;
    static int[] lazy;

    static int I (int s, int e, int tree_idx) {
        if (s == e) {
            fake[tree_idx] = 1;
            return 1;
        }

        int mid = (s + e) / 2;
        fake[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
        return fake[tree_idx];
    }

    static void lazy_U (int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            tree[tree_idx] = fake[tree_idx] - tree[tree_idx];
            if (s != e) {
                lazy[tree_idx*2] = 1 - lazy[tree_idx*2];
                lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1];
            }
            lazy[tree_idx] = 0;
        }
    }

    static int S (int s, int e, int tree_idx, int l, int r) {
        lazy_U(s, e, tree_idx);

        if (e < l || s > r) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        int mid = (s + e) / 2;
        return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
    }

    static void U (int s, int e, int tree_idx, int l, int r) {
        lazy_U(s, e, tree_idx);

        if (e < l || s > r) {
            return;
        }

        if (s >= l && e <= r) {
            tree[tree_idx] = fake[tree_idx] - tree[tree_idx];
            if (s != e) {
                lazy[tree_idx*2] = 1 - lazy[tree_idx*2];
                lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1];
            }
            return;
        }

        int mid = (s + e) / 2;
        U(s, mid, tree_idx*2, l, r);
        U(mid+1, e, tree_idx*2+1, l, r);

        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        fake = new int[4*N+1];
        lazy = new int[4*N+1];
        tree = new int[4*N+1];

        I(1, N, 1);

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            int o = Integer.parseInt(temp[0]);
            int s = Integer.parseInt(temp[1]);
            int t = Integer.parseInt(temp[2]);

            if (o == 0) {
                U(1, N, 1, s, t);
            }
            else {
                System.out.println(S(1, N, 1, s, t));
            }
        }
    }
}