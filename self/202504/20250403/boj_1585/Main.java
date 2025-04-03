import java.io.*;
import java.util.*;

public class Main {

    static int N, T, K, src, sink, ans;
    static int[] time_in, time_out, pre, dist, checker;
    static int[][] D, F, C;
    static List<Integer>[] G;
    static boolean isPossible;

    static int fee(int t, int s, int f) {
        if (t > s) {
            if ((t-s)*(t-s) > f) {
                return f;
            }
            else {
                return (t-s)*(t-s);
            }
        }
        else {
            return 0;
        }
    }

    static void solve() {
        src = 2*N+1; sink = 2*N+2;
        G = new ArrayList[2*N+3]; for (int idx = 0; idx < 2*N+3; ++idx) G[idx] = new ArrayList<Integer>();
        D = new int[2*N+3][2*N+3]; F = new int[2*N+3][2*N+3]; C = new int[2*N+3][2*N+3];

        for (int i = 0; i < N; ++i) {
            int u = i+1;
            G[src].add(u); G[u].add(src); C[src][u] = 1;
            G[u+N].add(sink); G[sink].add(u+N); C[u+N][sink] = 1;

            for (int j = 0; j < N; ++j) {
                int v = N+j+1;

                if (time_out[j] - time_in[i] > 0) {
                    int f = fee(T, time_out[j] - time_in[i], K);
                    G[u].add(v); G[v].add(u); C[u][v] = 1; D[u][v] = f; D[v][u] = -f;
                }
            }
        }

        pre = new int[2*N+3]; dist = new int[2*N+3]; checker = new int[2*N+3];
        isPossible = true; ans = 0;
        for (int i = 0; i < N; ++i) {
            Arrays.fill(pre, -1); Arrays.fill(dist, (1<<30)-1); Arrays.fill(checker, 0);
            Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); checker[src] = 1; dist[src] = 0;
            
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
            
            if (pre[sink] == -1) {
                isPossible = !isPossible; break;
            }
            
            for (int n = sink; n != src; n = pre[n]) {
                ++F[pre[n]][n]; --F[n][pre[n]]; ans += D[pre[n]][n];
            }
        }
        
        if (isPossible) System.out.printf("%d ", ans);
        else {
            System.err.println(-1);
            System.exit(1);
        }
        
        F = new int[2*N+3][2*N+3]; ans = 0;
        
        for (int i = 0; i < N; ++i) {
            Arrays.fill(pre, -1); Arrays.fill(dist, (1<<30)-1); Arrays.fill(checker, 0);
            Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); checker[src] = 1; dist[src] = 0;
            
            while (!q.isEmpty()) {
                int n = q.poll(); checker[n] = 0;

                for (int x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] - D[n][x]) {
                        dist[x] = dist[n] - D[n][x]; pre[x] = n;

                        if (checker[x] == 0) {
                            checker[x] = 1; q.offer(x);
                        }
                    }
                }
            }

            for (int n = sink; n != src; n = pre[n]) {
                ++F[pre[n]][n]; --F[n][pre[n]]; ans -= D[pre[n]][n];
            }
        }

        System.out.println(-ans);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String[] timein = br.readLine().split(" "); time_in = new int[N];
        for (int idx = 0; idx < N; ++idx) time_in[idx] = Integer.parseInt(timein[idx]);
        String[] timeout = br.readLine().split(" "); time_out = new int[N];
        for (int idx = 0; idx < N; ++idx) time_out[idx] = Integer.parseInt(timeout[idx]);
        T = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        solve();
    }
}