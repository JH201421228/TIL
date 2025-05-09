import java.io.*;
import java.util.*;

public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int N, src, sink, ans = 0;
    static int[] pre, indx, dist, checker, stories = new int[3];
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, -d, G[v].size()));
        G[v].add(new Edge(u, 0, d, G[u].size()-1));

        return;
    }

    static void solve() {
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

            for (int n = sink; n != src; n = pre[n]) {
                Edge edge = G[pre[n]].get(indx[n]);
                --edge.c;
                ++G[n].get(edge.inv).c;
            }

            ans += dist[sink];
        }

        System.out.println(-ans - 3000000);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        src = N+5; sink = N+6;
        G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();
        pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1]; indx = new int[sink+1];

        String[] temp = br.readLine().split(" "); for (int idx = 0; idx < 3; ++idx) stories[idx] = Integer.parseInt(temp[idx]);

        for (int v = 1; v < 4; ++v) {
            set_edge(src, v, 1, 1000000);
            set_edge(src, v, stories[v-1]-1, 0);
        }
        set_edge(src, 4, Integer.MAX_VALUE, 0);

        for (int u = 5; u < N+5; ++u) {
            String[] tmp = br.readLine().split(" ");
            
            set_edge(u, sink, 1, 0);

            for (int v = 1; v < 4; ++v) set_edge(v, u, 1, Integer.parseInt(tmp[v-1]));
            set_edge(4, u, 1, 0);
        }

        solve();

        return;
    }
}
