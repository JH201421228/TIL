import java.io.*;
import java.util.*;

public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int[][] delta = {{1, 0}, {0, 1}}, maze;
    static int N, K, src, sink, ans;
    static int[] pre, dist, indx, checker;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, -d, G[v].size()));
        G[v].add(new Edge(u, 0, d, G[u].size()-1));

        return;
    }

    static int solve() {
        Arrays.fill(pre, -1); Arrays.fill(checker, 0); Arrays.fill(indx, -1); Arrays.fill(dist, Integer.MAX_VALUE);
        Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); dist[src] = 0; checker[src] = 1;

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

        if (dist[sink] == Integer.MAX_VALUE) return 0;

        for (int n = sink; n != src; n = pre[n]) {
            Edge edge = G[pre[n]].get(indx[n]);
            --edge.c;
            ++G[n].get(edge.inv).c;
        }

        return dist[sink];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NK = br.readLine().split(" "); N = Integer.parseInt(NK[0]); K = Integer.parseInt(NK[1]);

        maze = new int[N][N];
        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < N; ++j) {
                maze[i][j] = Integer.parseInt(temp[j]);
            }
        }

        src = 2; sink = (N*N)<<1|1;
        G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();
        pre = new int[sink+1]; dist = new int[sink+1]; indx = new int[sink+1]; checker = new int[sink+1];

        for (int n = 1; n < N*N+1; ++n) {
            set_edge(n<<1, n<<1|1, 1, maze[((n-1)/N)][(n-1)%N]);
            set_edge(n<<1, n<<1|1, Integer.MAX_VALUE, 0);
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int u = N*i+j+1;
                for (int[] dd : delta) {
                    int ii = i+dd[0]; int jj = j+dd[1];
                    if (ii >= 0 && ii < N && jj >= 0 && jj < N) {
                        int v = N*ii+jj+1;
                        set_edge(u<<1|1, v<<1, Integer.MAX_VALUE, 0);
                    }
                }
            }
        }

        ans = 0;

        while (K-- > 0) {
            ans += solve();
        }

        System.out.println(-ans);
    }
}