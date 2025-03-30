import java.io.*;
import java.util.*;

public class Main {
    
    static int N, M, ans = 0;
    static int[] pre, dist, checker;
    static int[][] C, D, F;
    static List<Integer>[] G;

    static void setVertex(int n) {
        G[n].add(n+N); G[n+N].add(n); C[n][n+N] = (1<<31)-1;
    }

    static void setEdge(int u, int v, int c) {
        G[u+N].add(v); G[v].add(u+N); C[u+N][v] = 1; D[u+N][v] = c; D[v][u+N] = -c;
        G[v+N].add(u); G[u].add(v+N); C[v+N][u] = 1; D[v+N][u] = c; D[u][v+N] = -c;
    }

    static void solve() {
        for (int z = 0; z < 2; ++z) {
            Arrays.fill(pre, -1); Arrays.fill(dist, (1<<31)-1); Arrays.fill(checker, 0);
            Queue<Integer> q = new LinkedList<Integer>(); q.add(1); checker[1] = 1; dist[1] = 0;

            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        pre[x] = n; dist[x] = dist[n] + D[n][x];

                        if (checker[x] == 0) {
                            q.add(x); checker[x] = 1;
                        }
                    }
                }
            }

            for (int n = 2*N; n != 1; n = pre[n]) {
                F[pre[n]][n] += 1; F[n][pre[n]] -= 1; ans += D[pre[n]][n];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        G = new ArrayList[2*N+1]; for (int idx = 0; idx < 2*N+1; ++idx) G[idx] = new ArrayList<Integer>();
        C = new int[2*N+1][2*N+1]; D = new int[2*N+1][2*N+1]; F = new int[2*N+1][2*N+1];
        pre = new int[2*N+1]; dist = new int[2*N+1]; checker = new int[2*N+1];

        for (int n = 1; n < N+1; ++n) setVertex(n);

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            setEdge(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]), Integer.parseInt(temp[2]));
        }

        solve();

        System.out.println(ans);
    }
}