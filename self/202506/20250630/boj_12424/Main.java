import java.io.*;
import java.util.*;

public class Main {
    static class Edge {
        int x, d, inv;
        long c;
        Edge(int x, long c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int src = 7, sink = 8, T;
    static long N, A, B, C, D, E, F;
    static int[] pre, indx, checker;
    static long[] dist;
    static int[][] arr;
    static List<Edge>[] G;
    static long MAXV = Long.MAX_VALUE;

    static void set_edge(int u, int v, long c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static long spfa() {
        long res = 0;

        while (true) {
            Arrays.fill(pre, -1); Arrays.fill(indx, -1); Arrays.fill(checker, 0); Arrays.fill(dist, MAXV);
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

            long flow = MAXV;
            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                flow = Math.min(flow, edge.c);
            }

            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                edge.c -= flow;
                G[n].get(edge.inv).c += flow;
            }

            res -= flow * dist[sink];
        }

        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; ++t) {
            String[] temp = br.readLine().split(" ");
            N = Long.parseLong(temp[0]);
            A = Long.parseLong(temp[1]);
            B = Long.parseLong(temp[2]);
            C = Long.parseLong(temp[3]);
            D = Long.parseLong(temp[4]);
            E = Long.parseLong(temp[5]);
            F = Long.parseLong(temp[6]);

            arr = new int[3][3];

            for (int i = 0; i < 3; ++i) {
                String[] tmp = br.readLine().split(" ");
                for (int j = 0; j < 3; ++j) {
                    arr[i][j] = Integer.parseInt(tmp[j]);
                }
            }

            G = new List[9]; for (int idx = 0; idx < 9; ++idx) G[idx] = new ArrayList<Edge>();
            pre = new int[9]; checker = new int[9]; indx = new int[9]; dist = new long[9];

            set_edge(src, 1, A, 0);
            set_edge(src, 2, B, 0);
            set_edge(src, 3, C, 0);

            set_edge(4, sink, D, 0);
            set_edge(5, sink, E, 0);
            set_edge(6, sink, F, 0);

            for (int u = 0; u < 3; ++u) {
                for (int v = 0; v < 3; ++v) {
                    set_edge(u+1, v+4, N, -arr[u][v]);
                }
            }

            System.out.println("Case #" + t + ": " + spfa());
        }
    }
}
