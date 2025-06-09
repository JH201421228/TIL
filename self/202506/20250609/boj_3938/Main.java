import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int src = 366<<1, sink = 366<<1|1, ans, N;
    static int[] pre, dist, indx, checker;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, -d, G[v].size()));
        G[v].add(new Edge(u, 0, d, G[u].size()-1));

        return;
    }

    static int spfa() {
        ans = 0;

        pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1]; indx = new int[sink+1];
        while (true) {
            Arrays.fill(pre, -1); Arrays.fill(indx, -1); Arrays.fill(checker, 0); Arrays.fill(dist, Integer.MAX_VALUE);
            Queue<Integer> q = new LinkedList<>(); q.offer(src); dist[src] = 0; checker[src] = 1;

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

        return -ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            N = Integer.parseInt(br.readLine());
            if (N == 0) break;

            G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<>();

            set_edge(src, 1<<1, 2, 0);
            set_edge(365<<1|1, sink, 2, 0);
            for (int i = 1; i < 366; ++i) set_edge(i<<1, i<<1|1, Integer.MAX_VALUE, 0);
            for (int u = 1; u < 365; ++u) set_edge(u<<1|1, (u+1)<<1, Integer.MAX_VALUE, 0);
            for (int i = 0; i < N; ++i) {
                String[] temp = br.readLine().split(" "); int a = Integer.parseInt(temp[0]), b = Integer.parseInt(temp[1]), c = Integer.parseInt(temp[2]);
                set_edge(a<<1, b<<1|1, 1, c);
            }

            System.out.println(spfa());
        }

        return;
    }
}