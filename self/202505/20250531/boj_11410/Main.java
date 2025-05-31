import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;
        
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int src, sink, N, P, ans;
    static int[] pre, dist, checker, indx;
    static int[][] clients, fees;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, -d, G[v].size()));
        G[v].add(new Edge(u, 0, d, G[u].size()-1));

        return;
    }

    static void solve() {
        pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1]; indx = new int[sink+1];
    
        while (true) {
            Arrays.fill(pre, -1); Arrays.fill(dist, Integer.MAX_VALUE); Arrays.fill(checker, 0); Arrays.fill(indx, -1);
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

            int flow = Integer.MAX_VALUE;
            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                flow = Math.min(flow, edge.c);
            }

            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                edge.c -= flow;
                G[n].get(edge.inv).c += flow;
            }

            ans += flow*dist[sink];
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NP = br.readLine().split(" "); N = Integer.parseInt(NP[0]); P = Integer.parseInt(NP[1]);
        src = N+1; sink = N+2; ans = 0;

        G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();

        set_edge(src, 1, P, 0); set_edge(N, sink, P, 0);
        for (int u = 1; u < N; ++u) set_edge(u, u+1, Integer.MAX_VALUE, 0);
    

        clients = new int[N-1][N-1]; fees = new int[N-1][N-1];

        for (int i = 0; i < N-1; ++i) {
            String[] client = br.readLine().split(" ");
            for (int j = 0; j < N-1-i; ++j) clients[i][j] = Integer.parseInt(client[j]);
        }

        for (int i = 0; i < N-1; ++i) {
            String[] fee = br.readLine().split(" ");
            for (int j = 0; j < N-1-i; ++j) fees[i][j] = Integer.parseInt(fee[j]);
        }

        for (int u = 1; u < N; ++u) {
            for (int v = u+1; v < N+1; ++v) set_edge(u, v, clients[u-1][v-u-1], fees[u-1][v-u-1]);
        }

        solve();

        System.out.println(-ans);

        return;
    }    
}
