import java.util.*;
import java.io.*;


public class Main {

    static int[] arr;
    static int[] lazy;
    static int[] tree;

    static int I (int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        int mid = (s + e) / 2;

        tree[tree_idx] = I(s, mid, tree_idx*2) ^ I(mid+1, e, tree_idx*2+1);

        return tree[tree_idx];
    }

    static void lazy_U (int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            if (((e-s+1) % 2) != 0) {
                tree[tree_idx] ^= lazy[tree_idx];
            }
            if (s != e) {
                lazy[tree_idx*2] ^= lazy[tree_idx];
                lazy[tree_idx*2+1] ^= lazy[tree_idx];
            }
            lazy[tree_idx] = 0;
        }
    }

    static int S (int s, int e, int tree_idx, int l, int r) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        int mid = (s + e) / 2;

        return S(s, mid, tree_idx*2, l, r) ^ S(mid+1, e, tree_idx*2+1, l, r);
    }

    static void U(int s, int e, int tree_idx, int l, int r, int val) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            if (((e-s+1) % 2) != 0) {
                tree[tree_idx] ^= val;
            }
            if (s != e) {
                lazy[tree_idx*2] ^= val;
                lazy[tree_idx*2+1] ^= val;
            }
            return;
        }

        int mid = (s + e) / 2;

        U(s, mid, tree_idx*2, l, r, val);
        U(mid+1, e, tree_idx*2+1, l, r, val);

        tree[tree_idx] = tree[tree_idx*2] ^ tree[tree_idx*2+1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        arr = new int[N+1];
        tree = new int[4*N+1];
        lazy = new int[4*N+1];

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
                U(1, N, 1, Integer.parseInt(temp[1])+1, Integer.parseInt(temp[2])+1, Integer.parseInt(temp[3]));
            }
            else {
                System.out.println(S(1, N, 1, Integer.parseInt(temp[1])+1, Integer.parseInt(temp[2])+1));
            }
        }
    }
}