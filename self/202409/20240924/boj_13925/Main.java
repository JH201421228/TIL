package boj_13925;

import java.util.*;
import java.io.*;

public class Main {
    static long[] arr;
    static long[][] lazy;
    static long[] tree;

    static long MOD = 1000000007;

    static long I(int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        int mid = (s + e) / 2;

        tree[tree_idx] = (I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)) % MOD;
        
        return tree[tree_idx];
    }

    static void lazy_U(int s, int e, int tree_idx) {
        if (lazy[tree_idx][0] != 1 || lazy[tree_idx][1] != 0) {
            tree[tree_idx] = (tree[tree_idx] * lazy[tree_idx][0] + (e-s+1) * lazy[tree_idx][1]) % MOD;
            if (s != e) {
                lazy[tree_idx*2][0] = (lazy[tree_idx*2][0] * lazy[tree_idx][0]) % MOD;
                lazy[tree_idx*2][1] = (lazy[tree_idx*2][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD;
                lazy[tree_idx*2+1][0] = (lazy[tree_idx*2+1][0] * lazy[tree_idx][0]) % MOD;
                lazy[tree_idx*2+1][1] = (lazy[tree_idx*2+1][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD;
            }
            lazy[tree_idx][0] = 1;
            lazy[tree_idx][1] = 0;
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

        int mid = (s + e) / 2;

        return (S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)) % MOD;
    }

    static void U(int s, int e, int tree_idx, int l, int r, long v1, long v2) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            lazy[tree_idx][0] = (lazy[tree_idx][0] * v1) % MOD;
            lazy[tree_idx][1] = (lazy[tree_idx][1] * v1 + v2) % MOD;
            lazy_U(s, e, tree_idx);
            return;
        }

        int mid = (s + e) / 2;

        U(s, mid, tree_idx*2, l, r, v1, v2);
        U(mid+1, e, tree_idx*2+1, l, r, v1, v2);

        tree[tree_idx] = (tree[tree_idx*2] + tree[tree_idx*2+1]) % MOD;
    }
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        arr = new long[N+1];
        tree = new long[4*N+1];
        lazy = new long[4*N+1][2];

        for (int i = 0; i < 4*N+1; ++i) {
            lazy[i][0] = 1;
            lazy[i][1] = 0;
        }

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            arr[i+1] = Integer.parseInt(input[i]);
        }

        I(1, N, 1);

        int M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]);

            if (a == 1) {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);
                long d = Long.parseLong(temp[3]);

                U(1, N, 1, b, c, 1, d);
            }
            else if (a == 2) {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);
                long d = Long.parseLong(temp[3]);

                U(1, N, 1, b, c, d, 0);
            }
            else if (a == 3) {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);
                long d = Long.parseLong(temp[3]);
                
                U(1, N, 1, b, c, 0, d);
            }
            else {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);
                System.out.println(S(1, N, 1, b, c));
            }
        }
    }
}
