import java.io.*;
import java.util.*;


public class Main {
    static int[] arr;
    static int[] A;
    static int[] E;
    static int cnt = 0;
    static List<Integer>[] G;
    static int[] lazy;
    static int[] tree;

    static void dfs(int n) {
        A[n] = ++cnt;
        for (int x : G[n]) {
            dfs(x);
        }
        E[n] = cnt;
    }

    static void lazy_U(int s, int e, int idx) {
        if (lazy[idx] != 0) {
            if (s == e) {
                tree[idx] += lazy[idx];
            }
            else {
                lazy[idx*2] += lazy[idx];
                lazy[idx*2+1] += lazy[idx];
            }
            lazy[idx] = 0;
        }
    }

    static void U(int s, int e, int idx, int l, int r, int v) {
        lazy_U(s, e, idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            lazy[idx] += v;
            lazy_U(s, e, idx);
            return;
        }

        int mid = (s+e) >> 1;
        U(s, mid, idx*2, l, r, v);
        U(mid+1, e, idx*2+1, l, r, v);
    }

    static int S(int s, int e, int idx, int i) {
        lazy_U(s, e, idx);

        if (s > i || e < i) {
            return 0;
        }

        if (s == e) {
            return tree[idx];
        }

        int mid = (s+e) >> 1;
        
        return S(s, mid, idx*2, i) + S(mid+1, e, idx*2+1, i);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }
        A = new int[N+1];
        E = new int[N+1];
        tree = new int[4*N+1];
        lazy = new int[4*N+1];

        String[] arr = br.readLine().split(" ");
        for (int i = 1; i < N; ++i) {
            int a = Integer.parseInt(arr[i]);
            G[a].add(i+1);
        }

        dfs(1);

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");

            if (Integer.parseInt(temp[0]) == 1) {
                int a = Integer.parseInt(temp[1]), b = Integer.parseInt(temp[2]);
                U(1, N, 1, A[a], E[a], b);
            }
            else {
                int a = Integer.parseInt(temp[1]);
                System.out.println(S(1, N, 1, A[a]));
            }
        }
    }
}