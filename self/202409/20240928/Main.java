import java.util.*;
import java.io.*;


public class Main {
    static int MAX = 100000;
    static int[] tree = new int[4*MAX+1];
    static int[] lazy = new int[4*MAX+1];

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

    static int S(int s, int e, int tree_idx, int idx) {
        lazy_U(s, e, tree_idx);

        if (idx > e || idx < s) {
            return 0;
        }

        if (s == e) {
            return tree[tree_idx];
        }

        int mid = (s + e) / 2;

        return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx);
    }

    static void U(int s, int e, int tree_idx, int l, int r, int v) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            lazy[tree_idx] += v;
            lazy_U(s, e, tree_idx);
            return;
        }

        int mid = (s + e) / 2;

        U(s, mid, tree_idx*2, l, r, v);
        U(mid+1, e, tree_idx*2+1, l, r, v);

        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]), b = Integer.parseInt(temp[1]);

            System.out.println(S(1, MAX, 1, a) + S(1, MAX, 1, b));

            U(1, MAX, 1, a, b, 1);
            U(1, MAX, 1, a, a, -S(1, MAX, 1, a));
            U(1, MAX, 1, b, b, -S(1, MAX, 1, b));
        }
    }
}