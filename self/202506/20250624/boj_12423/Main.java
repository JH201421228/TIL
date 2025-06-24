import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int A, B, C, D, E, F, N, T, src = 7, sink = 8;
    static int[] pre, dist, checker, indx;
    static int[][] arr = new int[3][3];
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static int spfa() {
        int res = 0;

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
                            checker[edge.x] = 1; q.add(edge.x);
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

            res -= flow*dist[sink];
        }

        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; ++t) {
            String[] input = br.readLine().split(" ");
            N = Integer.parseInt(input[0]); A = Integer.parseInt(input[1]); B = Integer.parseInt(input[2]); C = Integer.parseInt(input[3]); D = Integer.parseInt(input[4]); E = Integer.parseInt(input[5]); F = Integer.parseInt(input[6]);  

            for (int i = 0; i < 3; ++i) {
                String[] temp = br.readLine().split(" ");
                for (int j = 0; j < 3; ++j) {
                    arr[i][j] = Integer.parseInt(temp[j]);
                }
            }
            pre = new int[9]; dist = new int[9]; checker = new int[9]; indx = new int[9];
            G = new List[9]; for (int idx = 0; idx < 9; ++idx) G[idx] = new ArrayList<Edge>();

            set_edge(src, 1, A, 0); set_edge(src, 2, B, 0); set_edge(src, 3, C, 0);
            set_edge(4, sink, D, 0); set_edge(5, sink, E, 0); set_edge(6, sink, F, 0);

            for (int u = 0; u < 3; ++u) {
                for (int v = 0; v < 3; ++v) {
                    set_edge(u+1, v+4, Integer.MAX_VALUE, -arr[u][v]);
                }
            }

            System.out.println("Case #" + t + ": " + spfa());
        }

        return;
    }    
}
