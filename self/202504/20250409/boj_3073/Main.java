import java.io.*;
import java.util.*;

public class Main {
    static int N, M, src, sink, ans;
    static char[][] maps;
    static List<int[]> homes, children;
    static List<Integer> G[];
    static int[][] F, C, D;
    static int[] pre, dist, checker;

    static void solve(BufferedReader br) throws IOException {
        maps = new char[N][M]; homes = new ArrayList<>(); children = new ArrayList<>();
    
        for (int i = 0; i < N; ++i) {
            String temp = br.readLine();
            for (int j = 0; j < M; ++j) {
                maps[i][j] = temp.charAt(j);
                
                if (temp.charAt(j) == 'H') homes.add(new int[] {i, j});
                else if (temp.charAt(j) == 'm') children.add(new int[] {i, j});
            }
        }

        int n = homes.size(); int m = children.size(); src = n+m+1; sink = n+m+2;
        G = new ArrayList[sink+1]; for (int i = 0; i < sink+1; ++i) G[i] = new ArrayList<Integer>();
        F = new int[sink+1][sink+1]; C = new int[sink+1][sink+1]; D = new int[sink+1][sink+1];

        for (int i = 0; i < n; ++i) {
            int u = i+1;
            G[src].add(u); G[u].add(src);
            C[src][u] = 1;
        }

        for (int i = 0; i < m; ++i) {
            int u = i+1+n;
            G[sink].add(u); G[u].add(sink);
            C[u][sink] = 1;
        }

        for (int i = 0; i < n; ++i) {
            int[] h = homes.get(i); int u = i+1;

            for (int j = 0; j < m; ++j) {
                int[] c = children.get(j); int v = j+1+n;

                G[u].add(v); G[v].add(u); C[u][v] = 1; D[u][v] = Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]); D[v][u] = -D[u][v];
            }
        }

        ans = 0;

        while (true) {
            pre = new int[sink+1]; Arrays.fill(pre, -1);
            dist = new int[sink+1]; Arrays.fill(dist, Integer.MAX_VALUE);
            checker = new int[sink+1];

            Queue<Integer> q = new LinkedList<Integer>(); q.add(src); dist[src] = 0; checker[src] = 1;

            while (!q.isEmpty()) {
                int cur = q.poll(); checker[cur] = 0;

                for (int x : G[cur]) {
                    if (C[cur][x] > F[cur][x] && dist[x] > dist[cur] + D[cur][x]) {
                        dist[x] = dist[cur] + D[cur][x]; pre[x] = cur;

                        if (checker[x] == 0) {
                            checker[x] = 1; q.add(x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int cur = sink; cur != src; cur = pre[cur]) {
                ++F[pre[cur]][cur]; --F[cur][pre[cur]]; ans += D[pre[cur]][cur];
            }
        }

        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {
            String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
            if (N == 0 || M == 0) break;

            solve(br);
        }
    }
}
