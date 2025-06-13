package boj_5892;

import java.io.*;
import java.util.*;

public class Main {
    
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static int src, sink, cur = 0, tar = 0, ans = 0, N, X, Y, Z;
    static int[] pre, dist, indx, checker;
    static List<Edge>[] G;

    static int solve() {
        while (true) {
            Arrays.fill(indx, -1); Arrays.fill(checker, 0); Arrays.fill(pre, -1); Arrays.fill(dist, Integer.MAX_VALUE);
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

            ans += dist[sink]*flow;
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NXYZ = br.readLine().split(" "); int N = Integer.parseInt(NXYZ[0]), X = Integer.parseInt(NXYZ[1]), Y = Integer.parseInt(NXYZ[2]), Z = Integer.parseInt(NXYZ[3]);

        src = (N+1)<<1; sink = (N+1)<<1|1;
        pre = new int[sink+1]; dist = new int[sink+1]; indx = new int[sink+1]; checker = new int[sink+1];
        G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();

        for (int i = 1; i < N+1; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]), b = Integer.parseInt(temp[1]);
            cur += a; tar += b;
            set_edge(src, i<<1, a, 0);
            set_edge(i<<1|1, sink, b, 0);
        }

        if (tar > cur) ans += (tar-cur)*X;
        else ans += (cur-tar)*Y;

        int fee = X+Y;
        for (int u = 1; u < N+1; ++u) {
            for (int v = 1; v < N+1; ++v) {
                int base = Math.abs(u-v)*Z;
                int charge = Math.min(fee, base);
                set_edge(u<<1, v<<1|1, Integer.MAX_VALUE, charge);
            }
        }

        System.out.println(solve());
    }
}