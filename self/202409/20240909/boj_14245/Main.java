package boj_14245;

import java.util.*;
import java.io.*;


public class Main {
    static int[] arr;
    static int[] lazy;

    static void lazy_U(int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            if (s == e) {
                arr[s] ^= lazy[tree_idx];
            }
            else {
                lazy[tree_idx*2] ^= lazy[tree_idx];
                lazy[tree_idx*2+1] ^= lazy[tree_idx];
            }
            lazy[tree_idx] = 0;
        }
    }

    static int S(int s, int e, int tree_idx, int idx) {
        lazy_U(s, e, tree_idx);

        if (s > idx || e < idx) {
            return 0;
        }

        if (s == e) {
            if (s == idx) {
                return arr[s];
            }
            else {
                return 0;
            }
        }

        int mid = (s + e) / 2;
        
        return S(s, mid, tree_idx*2, idx) ^ S(mid+1, e, tree_idx*2+1, idx);
    }

    static void U(int s, int e, int tree_idx, int l, int r, int val) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            if (s == e) {
                arr[s] ^= val;
            }
            else {
                lazy[tree_idx*2] ^= val;
                lazy[tree_idx*2+1] ^= val;
            }
            return;
        }

        int mid = (s + e) / 2;

        U(s, mid, tree_idx*2, l, r, val);
        U(mid+1, e, tree_idx*2+1, l, r, val);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N, M;

        N = Integer.parseInt(br.readLine());

        arr = new int[N+1];
        lazy = new int[4*N+1];

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            arr[i+1] = Integer.parseInt(input[i]);
        }

        M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            
            int t = Integer.parseInt(temp[0]);

            if (t == 1) {
                U(1, N, 1, Integer.parseInt(temp[1])+1, Integer.parseInt(temp[2])+1, Integer.parseInt(temp[3]));
            }
            else {
                System.out.println(S(1, N, 1, Integer.parseInt(temp[1])+1));
            }
        }
    }
}