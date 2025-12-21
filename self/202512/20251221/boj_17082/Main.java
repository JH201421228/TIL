package boj_17082;


import java.io.*;
import java.util.*;


public class Main {
    static int N, M, Q;
    static int[] arr, V, tree;
    static List<Integer> L, R;

    static int I(int s, int e, int tree_idx) {
        if (s == e) {
            if (V[s] == 1) tree[tree_idx] = arr[s];
            else tree[tree_idx] = Integer.MIN_VALUE;

            return tree[tree_idx];
        }

        int mid = (s+e) >> 1;

        return tree[tree_idx] = Math.max(I(s, mid, tree_idx*2), I(mid+1, e, tree_idx*2+1));
    }

    static int U(int s, int e, int idx, int tree_idx, int val) {
        if (s > idx || e < idx) return tree[tree_idx];

        if (s == e) {
            tree[tree_idx] = val;
            return val;
        }

        int mid = (s+e) >> 1;

        return tree[tree_idx] = Math.max(U(s, mid, idx, tree_idx*2, val), U(mid+1, e, idx, tree_idx*2+1, val));
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NMQ = br.readLine().split(" ");
        N = Integer.parseInt(NMQ[0]); M = Integer.parseInt(NMQ[1]); Q = Integer.parseInt(NMQ[2]);
        arr = new int[N+1];
        V = new int[N+1];
        tree = new int[4*N+1];

        String[] temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) arr[idx+1] = Integer.parseInt(temp[idx]);

        L = new ArrayList<Integer>();
        R = new ArrayList<Integer>();

        String[] temp_l = br.readLine().split(" ");
        String[] temp_r = br.readLine().split(" ");

        for (int idx = 0; idx < M; ++idx) {
            L.add(Integer.parseInt(temp_l[idx]));
            R.add(Integer.parseInt(temp_r[idx]));
        }

        L.sort((a, b) -> Integer.compare(a, b));
        R.sort((a, b) -> Integer.compare(a, b));

        int cur_idx = 0;
        for (int idx = 0; idx < M; ++idx) {
            if (L.get(idx) > R.get(idx)) {
                for (int i = 0; i < Q; ++i) System.out.println(1_000_000_000);
                return;
            }

            int l = Math.max(cur_idx, L.get(idx));
            int r = Math.max(cur_idx, R.get(idx));

            for (int i = l; i < r+1; ++i) V[i] = 1;

            cur_idx = r;
        }

        I(1, N, 1);

        for (int i = 0; i < Q; ++i) {
            String[] xy = br.readLine().split(" ");
            int x = Integer.parseInt(xy[0]); int y = Integer.parseInt(xy[1]);

            if (V[x] == 1) U(1, N, x, 1, arr[y]);
            else U(1, N, x, 1, Integer.MIN_VALUE);

            if (V[y] == 1) U(1, N, y, 1, arr[x]);
            else U(1, N, y, 1, Integer.MIN_VALUE);

            int temp_x = arr[x];
            arr[x] = arr[y];
            arr[y] = temp_x;

            System.out.println(tree[1]);
        }


        return;
    }
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}