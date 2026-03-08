package boj_11438;


import java.io.*;
import java.util.*;


public class Main {
    static int N, M;
    static int[] V, D;
    static int[][] A;
    static List<Integer>[] G;

    static void dfs(int cur, int depth) {
        D[cur] = depth;

        for (int x : G[cur]) {
            if (V[x] == 0) {
                V[x] = 1;
                A[x][0] = cur;
                
                dfs(x, depth+1);
            }
        }

        return;
    }

    static int LCA(int a, int b) {
        if (D[a] < D[b]) {
            int tmp = a; a = b; b = tmp;
        }

        if (D[a] != D[b]) {
            int diff = D[a] - D[b];

            for (int i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) a = A[a][i];
            }
        }

        if (a == b) return a;

        for (int i = 17; i >= 0; --i) {
            if (A[a][i] != A[b][i]) {
                a = A[a][i];
                b = A[b][i];
            }
        }

        return A[a][0];
    }

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        V = new int[N+1];
        D = new int[N+1];
        A = new int[N+1][18];
        G = new ArrayList[N+1]; for (int i = 0; i < N+1; ++i) G[i] = new ArrayList<>();

        for (int i = 0; i < N-1; ++i) {
            String[] temp = br.readLine().split(" ");
            int u = Integer.parseInt(temp[0]);
            int v = Integer.parseInt(temp[1]);

            G[u].add(v); G[v].add(u);
        }

        V[1] = 1;

        dfs(1, 0);

        for (int i = 1; i < 18; ++i) {
            for (int j = 1; j < N+1; ++j) {
                A[j][i] = A[A[j][i-1]][i-1];
            }
        }

        M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            int u = Integer.parseInt(temp[0]);
            int v = Integer.parseInt(temp[1]);

            System.out.println(LCA(u, v));
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
    
}