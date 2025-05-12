import java.io.*;
import java.util.*;

public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int N, M, src, sink, ans = 0;
    static int[] pre, dist, indx, checker;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static int solve() {
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

        if (pre[sink] == -1) return dist[sink];

        for (int n = sink; n != src; n = pre[n]) {
            Edge edge = G[pre[n]].get(indx[n]);
            --edge.c;
            ++G[n].get(edge.inv).c;
        }

        return dist[sink];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        G = new ArrayList[2*N+2]; for (int idx = 0; idx < 2*N+2; ++idx) G[idx] = new ArrayList<Edge>(); pre = new int[2*N+2]; indx = new int[2*N+2]; checker = new int[2*N+2]; dist = new int[2*N+2];

        for (int u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1 ,1, 0);

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" "); int a = Integer.parseInt(temp[0]), b = Integer.parseInt(temp[1]), c = Integer.parseInt(temp[2]);
            set_edge(b<<1|1, c<<1, 1, a);
            set_edge(c<<1|1, b<<1, 1, a);
        }

        String[] AB = br.readLine().split(" "); int A = Integer.parseInt(AB[0]), B = Integer.parseInt(AB[1]);
        src = A<<1;
        sink = B<<1|1;

        for (int i = 0; i < 2; ++i) ans += solve();
        
        if (ans == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(ans);;

        return;
    }
}
