import java.io.*;
import java.util.*;

public class Main {
    static int N, M, maxn = 1<<31-1, ans = 0, cnt = 0;
    static List<Integer>[] G;
    static int[][] F, C, D;
    static int[] pre, dist, checker;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        G = new ArrayList[N+M+3]; for (int i = 0; i < N+M+3; ++i) G[i] = new ArrayList<Integer>();
        F = new int[N+M+3][N+M+3];
        D = new int[N+M+3][N+M+3];
        C = new int[N+M+3][N+M+3];
        
        int src = N+M+1, sink = N+M+2;

        for (int u = 1; u < N+1; ++u) {
            G[src].add(u); G[u].add(src);
            C[src][u] = 1;
        }

        for (int u = N+1; u < N+M+1; ++u) {
            G[sink].add(u); G[u].add(sink);
            C[u][sink] = 1;
        }

        for (int u = 1; u < N+1; ++u) {
            String[] temp = br.readLine().split(" ");
            for (int i = 0; i < Integer.parseInt(temp[0]); ++i) {
                int v = Integer.parseInt(temp[i*2+1])+N, c = Integer.parseInt(temp[i*2+2]);
                G[u].add(v); G[v].add(u);
                C[u][v] = 1; D[u][v] = c; D[v][u] = -c;
            }
        }

        while (true) {
            pre = new int[N+M+3]; dist = new int[N+M+3]; checker = new int[N+M+3];
            Arrays.fill(pre, -1); Arrays.fill(dist, maxn);
            Queue<Integer> q = new LinkedList<Integer>(); q.offer(src);
            checker[src] = 1; dist[src] = 0;

            while (!q.isEmpty()) {
                int n = q.poll();
                checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x];
                        pre[x] = n;

                        if (checker[x] == 0) {
                            checker[x] = 1;
                            q.offer(x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int n = sink; n != src; n = pre[n]) {
                F[pre[n]][n] += 1;
                F[n][pre[n]] -= 1;
                ans += D[pre[n]][n];
            }
            ++cnt;
        }

        System.out.println(cnt);
        System.out.println(ans);
    }
}
