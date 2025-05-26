import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;
        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int src, sink, ans, N;
    static int[] pre, indx, checker, dist, A, H, L;
    static List<Edge>[] G;
    static List<int[]> arr = new ArrayList<int[]>();

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, d, G[v].size()));
        G[v].add(new Edge(u, 0, -d, G[u].size()-1));

        return;
    }

    static void solve() {
        ans = 0;
        pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1]; indx = new int[sink+1];
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

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N]; H = new int[N]; L = new int[N]; src = 2*N+2; sink = 2*N+3;
        G = new List[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Edge>();

        String[] A_temp = br.readLine().split(" "); String[] H_temp = br.readLine().split(" "); String[] L_temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) A[idx] = Integer.parseInt(A_temp[idx]);
        for (int idx = 0; idx < N; ++idx) L[idx] = Integer.parseInt(L_temp[idx]);
        for (int idx = 0; idx < N; ++idx) H[idx] = Integer.parseInt(H_temp[idx]);

        for (int idx = 0; idx < N; ++idx) arr.add(new int[] {A[idx], H[idx], L[idx]});

        arr.sort((a, b) -> Integer.compare(b[0], a[0]));

        set_edge(src, 1<<1, arr.get(0)[2], arr.get(0)[1]);
        for (int v = 2; v < N+1; ++v) set_edge(src, v<<1, arr.get(v-1)[2]-1, arr.get(v-1)[1]);
        for (int u = 2; u < N+1; ++u) set_edge(u<<1|1, sink, 1, arr.get(u-1)[1]);
        for (int u = 1; u < N+1; ++u) {
            for (int v = u+1; v < N+1; ++v) set_edge(u<<1, v<<1|1, 1, -(arr.get(u-1)[0]^arr.get(v-1)[0]));
        }

        solve();

        System.out.println(-ans);

        return;
    }    
}
