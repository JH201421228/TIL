import java.io.*;
import java.util.*;


public class Main {
    static int N, M, src, sink, ans = 0;
    static int[] pre, dist, checker, indx;
    static int[][] C, D, F;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size())); G[v].add(new Edge(u, 0, -d, G[u].size()-1));
    }

    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int solve() {
        Arrays.fill(pre, -1); Arrays.fill(dist, Integer.MAX_VALUE); Arrays.fill(indx, -1); Arrays.fill(checker, 0);
        Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); checker[src] = 1; dist[src] = 0;

        while(!q.isEmpty()) {
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

        for (int n = sink; n != src; n = pre[n] ) {
            --G[pre[n]].get(indx[n]).c; ++G[n].get(G[pre[n]].get(indx[n]).inv).c;
        }

        return dist[sink];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        
        src = 2; sink = N<<1|1; 
        pre = new int[(N+1)<<1]; dist = new int[(N+1)<<1]; indx = new int[(N+1)<<1]; checker = new int[(N+1)<<1];
        D = new int[(N+1)<<1][(N+1)<<1]; C = new int[(N+1)<<1][(N+1)<<1]; F = new int[(N+1)<<1][(N+1)<<1];
        G = new ArrayList[(N+1)<<1]; for (int idx = 0; idx < (N+1)<<1; ++idx) G[idx] = new ArrayList<Edge>();
        
        for (int n = 1; n < N+1; ++n) set_edge(n<<1, n<<1|1, Integer.MAX_VALUE, 0);;

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" "); int u = Integer.parseInt(temp[0]), v = Integer.parseInt(temp[1]), d = Integer.parseInt(temp[2]);
            set_edge(u<<1|1, v<<1, 1, d); set_edge(v<<1|1, u<<1, 1, d);
        }

        for (int i = 0; i < 2; ++i) ans += solve();

        System.out.println(ans);
    }
}
