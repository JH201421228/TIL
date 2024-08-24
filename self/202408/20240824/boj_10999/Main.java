package boj_10999;

import java.util.*;
import java.io.*;


public class Main {

    public static long[] arr;
    public static long[] tree;
    public static long[] lazy;

    public static long I(int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        int mid = (s+e) / 2;

        tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
        return tree[tree_idx];
    }

    public static void UU(int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            tree[tree_idx] += (e-s+1) * lazy[tree_idx];

            if (s != e) {
                lazy[tree_idx*2] += lazy[tree_idx];
                lazy[tree_idx*2+1] += lazy[tree_idx];
            }

            lazy[tree_idx] = 0;
        }
    }

    public static long S(int s, int e, int tree_idx, int l, int r) {
        UU(s, e, tree_idx);

        if (l > e || r < s) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        int mid = (s+e) / 2;
        return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
    }

    public static void U(int s, int e, int tree_idx, int l, int r, long c) {
        UU(s, e, tree_idx);

        if (l > e || r < s) {
            return;
        }

        if (s >= l && e <= r) {
            tree[tree_idx] += (e-s+1)*c;
            if (s != e) {
                lazy[tree_idx*2] += c;
                lazy[tree_idx*2+1] += c;
            }
            return;
        }

        int mid = (s+e) / 2;
        U(s, mid, tree_idx*2, l, r, c);
        U(mid+1, e, tree_idx*2+1, l, r, c);
        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]; 
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NMK = br.readLine().split(" ");
        int N = Integer.parseInt(NMK[0]);
        int M = Integer.parseInt(NMK[1]);
        int K = Integer.parseInt(NMK[2]);

        arr = new long[N+1];
        tree = new long[4*N+1];
        lazy = new long[4*N+1];

        for (int i = 0; i < N; ++i) {
            arr[i+1] = Long.parseLong(br.readLine());
        }

        I(1, N, 1);

        for (int i = 0; i < M+K; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]);

            if (a == 1) {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);
                long d = Long.parseLong(temp[3]);

                U(1, N, 1, b, c, d);
            }
            else {
                int b = Integer.parseInt(temp[1]);
                int c = Integer.parseInt(temp[2]);

                System.out.println(S(1, N, 1, b, c));
            }
        }
    }
}