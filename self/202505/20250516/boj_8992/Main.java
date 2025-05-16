package boj_8992;

import java.io.*;
import java.util.*;


public class Main {
    static class Edge {
        int x, c, d, inv;

        Edge(int x, int c, int d, int inv) {
            this.x = x; this.c = c; this.d = d; this.inv = inv;
        }
    }

    static int T, N, M, src, sink, ans, cnt;
    static int[] indx, checker, dist, pre;
    static int[][] vertical, horizontal;
    static List<Edge>[] G;

    static void set_edge(int u, int v, int c, int d) {
        G[u].add(new Edge(v, c, -d, G[v].size()));
        G[v].add(new Edge(u, 0, d, G[u].size()-1));

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        ans = 0; cnt = 0;

        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        G = new List[N+M+3]; for (int idx = 0; idx < N+M+3; ++idx) G[idx] = new ArrayList<Edge>();
        pre = new int[N+M+3]; dist = new int[N+M+3]; indx = new int[N+M+3]; checker = new int[N+M+3];

        src = N+M+1; sink = N+M+2;

        vertical = new int[M+1][5]; horizontal = new int[N+1][5];

        for (int i = 1; i < N+1; ++i) {
            String[] horiz = br.readLine().split(" ");
            for (int j = 0; j < 5; ++j) {
                horizontal[i][j] = Integer.parseInt(horiz[j]);
            }
        }

        for (int i = 1; i < M+1; ++i) {
            String[] verti = br.readLine().split(" ");
            for (int j = 0; j < 5; ++j) {
                vertical[i][j] = Integer.parseInt(verti[j]);
            }
        }

        for (int u = 1; u < N+1; ++u) {
            int ux1 = horizontal[u][0], uy1 = horizontal[u][1], ux2 = horizontal[u][2], uy2 = horizontal[u][3], uw = horizontal[u][4];
            set_edge(src, u, 1, 0);

            for (int v = N+1; v < M+N+1; ++v) {
                int vx1 = vertical[v-N][0], vy1 = vertical[v-N][1], vx2 = vertical[v-N][2], vy2 = vertical[v-N][3], vw = vertical[v-N][4];

                if (vx1 > Math.min(ux1, ux2) && vx1 < Math.max(ux1, ux2) && uy1 > Math.min(vy1, vy2) && uy1 < Math.max(vy1, vy2)) set_edge(u, v, 1, uw*vw);
            }
        }

        for (int v = N+1; v < M+N+1; ++v) set_edge(v, sink, 1, 0);

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

            ++cnt;

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

        T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            solve(br);

            System.out.print(cnt);
            System.out.print(" ");
            System.out.println(-ans);
        }

        return;
    }    
}