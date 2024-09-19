package boj_17353;

import java.io.*;
import java.util.*;


public class Main {
    static int[] arr;
    static int[] arr_;
    static long[] tree;
    static long[] lazy;

    static Long I (int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = (long) arr_[s];
            return (long) arr_[s];
        }

        int mid = (s + e) / 2;

        tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
        
        return tree[tree_idx];
    }

    static void lazy_U (int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            tree[tree_idx] += (e-s+1) * lazy[tree_idx];
            if (s != e) {
                lazy[tree_idx*2] += lazy[tree_idx];
                lazy[tree_idx*2+1] += lazy[tree_idx];
            }
            lazy[tree_idx] = 0;
        }
    }

    static long S (int s, int e, int tree_idx, int l, int r) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return (long) 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        int mid = (s + e) / 2;

        return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
    }

    static void U (int s, int e, int tree_idx, int l, int r, int val) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            tree[tree_idx] += (long) (e-s+1) * val;
            if (s != e) {
                lazy[tree_idx*2] += (long) val;
                lazy[tree_idx*2+1] += (long) val;
            }
            return;
        }

        int mid = (s + e) / 2;

        U(s, mid, tree_idx*2, l, r, val);
        U(mid+1, e, tree_idx*2+1, l, r, val);

        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N, Q;
        N = Integer.parseInt(br.readLine());

        arr = new int[N+1];
        arr_ = new int[N+1];
        tree = new long[4*N+1];
        lazy = new long[4*N+1];

        String[] input = br.readLine().split((" "));

        for (int i = 0; i < N; ++i) {
            arr[i+1] = Integer.parseInt(input[i]);
            arr_[i+1] = arr[i+1] - arr[i];
        }

        I(1, N, 1);

        Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; ++i) {
            String[] temp = br.readLine().split(" ");

            if (Integer.parseInt(temp[0]) == 1) {
                U(1, N, 1, Integer.parseInt(temp[1]), Integer.parseInt(temp[2]), 1);
                if (Integer.parseInt(temp[2]) != N) {
                    U(1, N, 1, Integer.parseInt(temp[2])+1, Integer.parseInt(temp[2])+1, -(Integer.parseInt(temp[2])-Integer.parseInt(temp[1])+1));
                }
            }
            else {
                System.out.println(S(1, N, 1, 1, Integer.parseInt(temp[1])));
            }
        }
    }
    
}