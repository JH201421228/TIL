import java.io.*;
import java.util.*;

public class Main {

    static int N, M, ans = 0, src, sink, maxv = (1<<31)-1;
    static int[] pre, dist, checker;
    static int[][] grades = {{10, 8, 7, 5, 1}, {8, 6, 4, 3, 1}, {7, 4, 3, 2, 1}, {5, 3, 2, 2, 1}, {1, 1, 1, 1, 0}}, F, D, C, delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    static Map<Character, Integer> T = new HashMap<>() {{put('A', 0); put('B', 1); put('C', 2); put('D', 3); put('F', 4);}};
    static Queue<Integer> q;
    static List<Integer> G[];
    static char[][] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        
        src = N*M+1; sink = N*M+2;
        G = new ArrayList[N*M+3]; for (int i = 0; i < N*M+3; ++i) G[i] = new ArrayList<Integer>();
        C = new int[N*M+3][N*M+3];
        F = new int[N*M+3][N*M+3];
        D = new int[N*M+3][N*M+3];
        B = new char[N][M];

        for (int i = 0; i < N; ++i) {
            String temp = br.readLine();
            for (int j = 0; j < M; ++j) {
                B[i][j] = temp.charAt(j);
            }
        }

        for (int i = 0; i < N; ++i) {
            for (int j = (i+1)%2; j < M; j+=2) {
                int v = i*M+j+1;

                G[v].add(sink); G[sink].add(v);
                C[v][sink] = 1;
            }

            for (int j = i%2; j < M; j+=2) {
                int u = i*M+j+1;
                
                G[src].add(u); G[u].add(src);
                G[u].add(sink); G[sink].add(u);
                C[u][sink] = 1; C[src][u] = 1;

                for (int[] d : delta) {
                    int xi = i+d[0], xj = j+d[1];
                    if (xi >= 0 && xi < N && xj >= 0 && xj < M) {
                        int v = xi*M+xj+1;

                        G[u].add(v); G[v].add(u);
                        C[u][v] = 1;
                        D[u][v] = -grades[T.get(B[i][j])][T.get(B[xi][xj])]; D[v][u] = -D[u][v];
                    }
                }
            }
        }

        pre = new int[N*M+3]; dist = new int[N*M+3]; checker = new int[N*M+3]; q = new LinkedList<Integer>();
        while (true) {
            Arrays.fill(pre, -1); Arrays.fill(dist, maxv); Arrays.fill(checker, 0);
            q.clear(); q.add(src); checker[src] = 1; dist[src] = 0;

            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x];
                        pre[x] = n;

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

        System.out.println(-ans);
    }
}
