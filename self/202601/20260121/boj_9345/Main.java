package boj_9345;

import java.io.*;
import java.util.*;


class Main {
    static int T, N, K, Q, A, B;
    static int[] arr = new int[100_001];
    static int[] max_tree = new int[400_005];
    static int[] min_tree = new int[400_005];

    static int I(int s, int e, int tree_idx, int flag, int[] tree) {
        if (s == e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        int mid = (s+e)>>1;

        if (flag == 1) tree[tree_idx] = Math.max(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));
        else tree[tree_idx] = Math.min(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));

        return tree[tree_idx];
    }


    static void U(int s, int e, int idx, int tree_idx, int flag, int[] tree) {
        if (idx > e || idx < s) return;

        if (s == e) {
            tree[tree_idx] = arr[idx];
            return;
        }

        int mid = (s+e)>>1;

        U(s, mid, idx, tree_idx<<1, flag, tree);
        U(mid+1, e, idx, tree_idx<<1|1, flag, tree);

        if (flag == 1) tree[tree_idx] = Math.max(tree[tree_idx<<1], tree[tree_idx<<1|1]);
        else tree[tree_idx] = Math.min(tree[tree_idx<<1], tree[tree_idx<<1|1]);

        return;
    }


    static int S(int s, int e, int l, int r, int tree_idx, int flag, int[] tree) {
        if (s >= l && e <= r) return tree[tree_idx];

        if (s > r || e < l) {
            if (flag == 1) return 0;
            else return Integer.MAX_VALUE;
        }

        int mid = (s+e)>>1;

        if (flag == 1) return Math.max(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
        else return Math.min(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
    }


    static void solve(BufferedReader br) throws IOException {
        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]);
        K = Integer.parseInt(NK[1]);

        for (int idx = 0; idx < N; ++idx) arr[idx] = idx;
        for (int idx = 0; idx < 4*N+1; ++idx) {
            max_tree[idx] = 0;
            min_tree[idx] = Integer.MAX_VALUE;
        }

        I(0, N-1, 1, 1, max_tree);
        I(0, N-1, 1, 0, min_tree);

        for (int i = 0; i < K; ++i) {
            String[] QAB = br.readLine().split(" ");
            Q = Integer.parseInt(QAB[0]);
            A = Integer.parseInt(QAB[1]);
            B = Integer.parseInt(QAB[2]);

            if (Q == 1) {
                if (A == S(0, N-1, A, B, 1, 0, min_tree) && B == S(0, N-1, A, B, 1, 1, max_tree)) System.out.println("YES");
                else System.out.println("NO");
            }
            else {
                int tmp = arr[A];
                arr[A] = arr[B];
                arr[B] = tmp;

                U(0, N-1, A, 1, 0, min_tree);
                U(0, N-1, B, 1, 0, min_tree);
                U(0, N-1, A, 1, 1, max_tree);
                U(0, N-1, B, 1, 1, max_tree);
            }
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; ++i) solve(br);

        return;
    }
}