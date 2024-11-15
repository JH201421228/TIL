import java.io.*;
import java.util.*;

public class Main {
    static long[] arr;
    static long[] tree;
    static long[] lazy;

    static long I(int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        int mid = (s + e) >> 1;

        tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);

        return tree[tree_idx];
    }

    static void lazy_U(int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            tree[tree_idx] += (e-s+1) * lazy[tree_idx];
            if (s != e) {
                lazy[tree_idx*2] += lazy[tree_idx];
                lazy[tree_idx*2+1] += lazy[tree_idx];
            }
            lazy[tree_idx] = 0;
        }
    }

    static long S(int s, int e, int tree_idx, int l, int r) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        int mid = (s + e) >> 1;

        return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
    }

    static void U(int s, int e, int tree_idx, int l, int r, int v) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            lazy[tree_idx] += (long) v;
            lazy_U(s, e, tree_idx);
            return;
        }

        int mid = (s + e) >> 1;

        U(s, mid, tree_idx*2, l, r, v);
        U(mid+1, e, tree_idx*2+1, l, r, v);
        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NQs = br.readLine().split(" ");
        int N = Integer.parseInt(NQs[0]), Q1 = Integer.parseInt(NQs[1]), Q2 = Integer.parseInt(NQs[2]);

        arr = new long[N+1];
        tree = new long[4*N+1];
        lazy = new long[4*N+1];

        String[] temp = br.readLine().split(" ");
        for (int i = 1; i < N+1; ++i) {
            arr[i] = Long.parseLong(temp[i-1]);
        }

        I(1, N, 1);

        for (int i = 0; i < Q1 + Q2; ++i) {
            String[] q = br.readLine().split(" ");

            if (Integer.parseInt(q[0]) == 1) {
                System.out.println(S(1, N, 1, Integer.parseInt(q[1]), Integer.parseInt(q[2])));
            }
            else {
                U(1, N, 1, Integer.parseInt(q[1]), Integer.parseInt(q[2]), Integer.parseInt(q[3]));
            }
        }
    }
}