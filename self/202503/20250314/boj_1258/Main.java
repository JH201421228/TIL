package boj_1258;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int N, ans = 0, maxv = (1 << 31) - 1;
    static int[] pre, dist, checker;
    static int[][] C, F, D;
    static List<Integer>[] G;
    static Queue<Integer> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int src = 2*N+1, sink = 2*N+2;

        G = new ArrayList[2*N+3]; for (int i = 0; i < 2*N+3; ++i) G[i] = new ArrayList<Integer>();
        C = new int[2*N+3][2*N+3];
        F = new int[2*N+3][2*N+3];
        D = new int[2*N+3][2*N+3];

        for (int u = 1; u < N+1; ++u) {
            int v = u + N;
            G[src].add(u); G[u].add(src); C[src][u] = 1;
            G[sink].add(v); G[v].add(sink); C[v][sink] = 1;
        }

        for (int u = 1; u < N+1; ++u) {
            String[] temp = br.readLine().split(" ");
            for (int i = 0; i < N; ++i) {
                int v = i+N+1, c = Integer.parseInt(temp[i]);
                G[u].add(v); G[v].add(u); C[u][v] = 1; D[u][v] = c; D[v][u] = -c;
            }
        }

        while (true) {
            pre = new int[2*N+3]; dist = new int[2*N+3]; checker = new int[2*N+3];
            Arrays.fill(pre, -1); Arrays.fill(dist, maxv);
            dist[src] = 0; checker[src] = 1;
            q = new LinkedList<Integer>(); q.offer(src);

            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n;

                        if (checker[x] == 0) {
                            checker[x] = 1; q.offer(x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int n = sink; n != src; n = pre[n]) {
                F[pre[n]][n] += 1; F[n][pre[n]] -= 1;
                ans += D[pre[n]][n];
            }
        }

        System.out.println(ans);
    }
}