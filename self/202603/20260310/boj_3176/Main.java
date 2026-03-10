package boj_3176;


import java.io.*;
import java.util.*;


public class Main {

    static int N, K;
    static int[] D, V;
    static int[][][] A;
    static List<int[]>[] G;


    static int[] LCA(int a, int b) {
        if (D[a] < D[b]) {
            int tmp = a;
            a = b; b = tmp;
        }

        int min_res = Integer.MAX_VALUE;
        int max_res = Integer.MIN_VALUE;

        if (D[a] != D[b]) {
            int diff = D[a] - D[b];
            for (int i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) {
                    max_res = Math.max(max_res, A[a][i][1]);
                    min_res = Math.min(min_res, A[a][i][2]);
                    a = A[a][i][0];
                }
            }
        }

        if (a == b) {
            if (min_res == Integer.MAX_VALUE) min_res = 0;
            if (max_res == Integer.MIN_VALUE) max_res = 0;

            return new int[] {min_res, max_res};
        }

        for (int i = 17; i >= 0; --i) {
            if (A[a][i][0] != A[b][i][0]) {
                max_res = Math.max(max_res, Math.max(A[a][i][1], A[b][i][1]));
                min_res = Math.min(min_res, Math.min(A[a][i][2], A[b][i][2]));

                a = A[a][i][0];
                b = A[b][i][0];
            }
        }

        max_res = Math.max(max_res, Math.max(A[a][0][1], A[b][0][1]));
        min_res = Math.min(min_res, Math.min(A[a][0][2], A[b][0][2]));

        if (min_res == Integer.MAX_VALUE) min_res = 0;
        if (max_res == Integer.MIN_VALUE) max_res = 0;

        return new int[] {min_res, max_res};
    }


    static void dfs(int cur, int depth) {
        D[cur] = depth;

        for (int[] x : G[cur]) {
            int nxt = x[0];
            int cost = x[1];

            if (V[nxt] != 1) {
                V[nxt] = 1;
                A[nxt][0][0] = cur;
                A[nxt][0][1] = cost;
                A[nxt][0][2] = cost;

                dfs(nxt, depth+1);
            }
        }

        return;
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        V = new int[N+1];
        D = new int[N+1];
        A = new int[N+1][18][3];
        G = new ArrayList[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<>();

        for (int idx = 0; idx < N+1; ++idx) {
            for (int jdx = 0; jdx < 18; ++jdx) {
                A[idx][jdx][1] = Integer.MIN_VALUE;
                A[idx][jdx][2] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < N-1; ++i) {
            String[] uvc = br.readLine().split(" ");
            int u, v, c;
            u = Integer.parseInt(uvc[0]);
            v = Integer.parseInt(uvc[1]);
            c = Integer.parseInt(uvc[2]);

            G[u].add(new int[] {v, c});
            G[v].add(new int[] {u, c});
        }

        V[1] = 1;
        dfs(1, 0);

        for (int i = 1; i < 18; ++i) {
            for (int j = 1; j < N+1; ++j) {
                A[j][i][0] = A[A[j][i-1][0]][i-1][0];
                A[j][i][1] = Math.max(A[A[j][i-1][0]][i-1][1], A[j][i-1][1]);
                A[j][i][2] = Math.min(A[A[j][i-1][0]][i-1][2], A[j][i-1][2]);
            }
        }

        K = Integer.parseInt(br.readLine());

        for (int i = 0; i < K; ++i) {
            String[] uv = br.readLine().split(" ");
            int u = Integer.parseInt(uv[0]);
            int v = Integer.parseInt(uv[1]);

            int[] res = LCA(u, v);

            System.out.println(res[0] + " " + res[1]);
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}