import java.io.*;
import java.util.*;

public class Main {
    static int N, M, maxv = 1<<9, ans = 0;
    static int[][] C, D, F;
    static List<Integer> G[];
    static int[] pre, dist, checker;
    static Queue<Integer> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        C = new int[203][203]; D = new int[203][203]; F = new int[203][203];
        G = new ArrayList[203]; for (int i = 0; i < 203; ++i) G[i] = new ArrayList<Integer>();
        
        String[] temp1 = br.readLine().split(" ");
        for (int u = 101; u < 101+N; ++u ) {
            G[u].add(202); G[202].add(u);
            C[u][202] = Integer.parseInt(temp1[u-101]);
        }

        String[] temp2 = br.readLine().split(" ");
        for (int v = 1; v < 1+M; ++v) {
            G[v].add(201); G[201].add(v);
            C[201][v] = Integer.parseInt(temp2[v-1]);
        }

        for (int u = 1; u < 1+M; ++u) {
            String[] temp3 = br.readLine().split(" ");
            for (int v = 101; v < 101+N; ++v) {
                D[u][v] = Integer.parseInt(temp3[v-101]); D[v][u] = -Integer.parseInt(temp3[v-101]);
                C[u][v] = maxv;
                G[u].add(v); G[v].add(u);
            }
        }

        while (true) {
            pre = new int[203]; Arrays.fill(pre, -1);        
            dist = new int[203]; Arrays.fill(dist, maxv);
            checker = new int[203];
            q = new LinkedList<Integer>(); q.add(201); checker[201] = 1; dist[201] = 0;

            while (!q.isEmpty()) {
                int n = q.poll();
                checker[n] = 1;

                for (int x : G[n]) {
                    if (C[n][x] - F[n][x] > 0 && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n;

                        if (checker[x] == 0) {
                            checker[x] = 1; q.offer(x);
                        }
                    }
                }
            }

            if (pre[202] == -1) break;

            int flow = maxv;
            for (int n = 202; n != 201; n = pre[n]) flow = Math.min(flow, C[pre[n]][n] - F[pre[n]][n]);

            for (int n = 202; n != 201; n = pre[n]) {
                ans += (flow * D[pre[n]][n]);
                F[pre[n]][n] += flow; F[n][pre[n]] -= flow;
            }
        }

        System.out.println(ans);
    }
}