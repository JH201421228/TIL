import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int T, ans, src, sink, N, M;
    static int[] pre, dist, indx, checker;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static int solve() {
        ans = 0;

        while (true) {
            Arrays.fill(pre, -1); Arrays.fill(indx, -1); Arrays.fill(checker, 0); Arrays.fill(dist, Integer.MAX_VALUE);
            Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); checker[src] = 1; dist[src] = 0;

            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int idx = 0; idx < G[n].size(); ++idx) {
                    Edge edge = G[n].get(idx);

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                        if (checker[edge.x] == 0) {
                            checker[edge.x] = 1; q.offer(edge.x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                --edge.c;
                ++G[n].get(edge.inv).c;
            }

            ans += dist[sink];
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
            src = 2*N+2; sink = 2*N+3;
            G = new List[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();
            pre = new int[sink+1]; indx = new int[sink+1]; checker = new int[sink+1]; dist = new int[sink+1];

            for (int u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1, Integer.MAX_VALUE, 0);

            for (int i = 0; i < M; ++i) {
                String[] xy = br.readLine().split(" "); int x = Integer.parseInt(xy[0]), y = Integer.parseInt(xy[1]);
                set_edge(x<<1|1, y<<1, Integer.MAX_VALUE, 1); set_edge(y<<1|1, x<<1, Integer.MAX_VALUE, 1);
            }

            String[] nodes = br.readLine().split(" ");
            for (int u = 1; u < N+1; ++u) {
                if (Integer.parseInt(nodes[u-1]) == 0) set_edge(u<<1|1, sink, 1, 0);
            }

            String[] coins = br.readLine().split(" ");
            for (int v = 1; v < N+1; ++v) {
                if (Integer.parseInt(coins[v-1]) == 0) set_edge(src, v<<1, 1, 0);
            }

            System.out.println(solve());
        }

        return;
    }
}