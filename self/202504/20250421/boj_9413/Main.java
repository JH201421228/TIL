import java.io.*;
import java.util.*;

public class Main {

    static int T, N, M, ans, src, sink;
    static List<Integer> G[];
    static int[][] C, D, F;
    static int[] pre, dist, checker;
    static Queue<Integer> q;

    static void set_edge(int u, int v) {
        G[u].add(v); G[v].add(u); C[u][v] = 1;
        
        return;
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NM = br.readLine().split(" "); int N = Integer.parseInt(NM[0]), M = Integer.parseInt(NM[1]); ans = 0; src = 2*N+1; sink = 2*N+2;

        G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Integer>();
        C = new int[sink+1][sink+1]; D = new int[sink+1][sink+1]; F = new int[sink+1][sink+1];

        for (int i = 1; i < N+1; ++i) {
            set_edge(i, i+N); set_edge(src, i); set_edge(i+N, sink);
            D[i][i+N] = -1; D[i+N][i] = 1;
        }

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]), v = Integer.parseInt(uv[1]);
            set_edge(u+N, v);
        }

        for (int i = 0; i < 2; ++i) {
            pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1]; Arrays.fill(pre, -1); Arrays.fill(checker, 0 ); Arrays.fill(dist, Integer.MAX_VALUE);
            q = new LinkedList<Integer>(); q.offer(src); checker[src] = 1; dist[src] = 0;

            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n;

                        if (checker[x] == 0) {
                            checker[x] = 1; q.offer(x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int n = sink; n != src; n = pre[n]) {
                F[pre[n]][n]++; F[n][pre[n]]--; ans += D[pre[n]][n];
            }
        }

        System.out.println(-ans);
        
        return;
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        T = Integer.parseInt(br.readLine());

        while (T-- > 0) solve(br);
    }
}