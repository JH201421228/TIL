package boj_13511;


import java.io.*;
import java.util.*;


public class Main {
    static int N, M;
    static int[] D, V;
    static long[][][] A;
    static List<int[]>[] G;


    static void dfs(int cur, int depth) {
        D[cur] = depth;

        for (int[] x : G[cur]) {
            int nxt = x[0];
            int cost = x[1];

            if (V[nxt] == 0) {
                V[nxt] = 1;
                A[nxt][0][0] = cur;
                A[nxt][0][1] = cost;

                dfs(nxt, depth+1);
            }
        }

        return;
    }


    static long[] LCA(int a, int b) {
        if (D[a] < D[b]) {
            int tmp = a;
            a = b; b = tmp;
        }

        long cost = 0;

        if (D[a] != D[b]) {
            int diff = D[a] - D[b];

            for (int i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) {
                    cost += A[a][i][1];
                    a = (int) A[a][i][0];
                }
            }
        }

        if (a == b) return new long[] {cost, a};

        for (int i = 17; i > -1; --i) {
            if (A[a][i][0] != A[b][i][0]) {
                cost += A[a][i][1];
                cost += A[b][i][1];

                a = (int) A[a][i][0];
                b = (int) A[b][i][0];
            }
        }

        cost += A[a][0][1];
        cost += A[b][0][1];

        return new long[] {cost, A[a][0][0]};
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        V = new int[N+1];
        D = new int[N+1];
        A = new long[N+1][18][2];
        G = new ArrayList[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<>();

        for (int i = 0; i < N-1; ++i) {
            String[] uvw = br.readLine().split(" ");
            int u = Integer.parseInt(uvw[0]);
            int v = Integer.parseInt(uvw[1]);
            int w = Integer.parseInt(uvw[2]);

            G[u].add(new int[] {v, w});
            G[v].add(new int[] {u, w});
        }

        V[1] = 1;
        dfs(1, 0);

        for (int i = 1; i < 18; ++i) {
            for (int j = 0; j < N+1; ++j) {
                A[j][i][0] = A[(int) A[j][i-1][0]][i-1][0];
                A[j][i][1] = A[j][i-1][1] + A[(int) A[j][i-1][0]][i-1][1];
            }
        }

        M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");

            int u = Integer.parseInt(temp[1]);
            int v = Integer.parseInt(temp[2]);

            long[] res = LCA(u, v);

            if (Integer.parseInt(temp[0]) == 1) System.out.println(res[0]);
            else {
                int k = Integer.parseInt(temp[3]); --k;

                int node = (int) res[1];

                if (D[u] - D[node] < k) {
                    k = D[u] + D[v] - 2*D[node] - k;
                    u = v;
                }

                for (int j = 17; j > -1; --j) {
                    if ((k & (1<<j)) > 0) u = (int) A[u][j][0];
                }

                System.out.println(u);
            }
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}