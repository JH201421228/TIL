import java.io.*;
import java.util.*;

public class Main {
    static int[][] satisfaction = {{4, 3, 2, 1}, {8, 7, 6, 5}, {12, 11, 10, 9}}, C, D, F;
    static int N, M, src, sink, ans;
    static int[] pre, dist, checker;
    static List<Integer>[] G;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {   
            String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

            if (N == 0 && M == 0) break;

            ans = 0; src = N+M+1; sink = N+M+2;
            G = new ArrayList[sink+1]; for (int idx = 0; idx < sink+1; ++idx) G[idx] = new ArrayList<Integer>();
            C = new int[sink+1][sink+1]; F = new int[sink+1][sink+1]; D = new int[sink+1][sink+1];
            
            for (int i = 0; i < N; ++i) {
                int u = i+M+1;
                C[u][sink] = Integer.parseInt(br.readLine());
                G[u].add(sink); G[sink].add(u);
            }
            
            for (int i = 0; i < M; ++i) {
                int u = i+1;
                
                C[src][u] = 1; G[src].add(u); G[u].add(src);
                
                String[] temp = br.readLine().split(" ");
                int grade = Integer.parseInt(temp[0]);
                
                for (int idx = 1; idx < 5; ++idx) {
                    int v = Integer.parseInt(temp[idx])+1+M;
                    G[u].add(v); G[v].add(u);
                    D[u][v] = -satisfaction[grade-1][idx-1]; D[v][u] = -D[u][v]; C[u][v] = 1;
                }
            }
            
            while (true) {
                pre = new int[sink+1]; dist = new int[sink+1]; checker = new int[sink+1];
                Arrays.fill(pre, -1); Arrays.fill(dist, Integer.MAX_VALUE); Arrays.fill(checker, 0);
                Queue<Integer> q = new LinkedList<Integer>(); q.offer(src); dist[src] = 0; checker[src] = 1;
                
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
                    F[pre[n]][n]++; F[n][pre[n]]--; ans += D[pre[n]][n];
                }
            }
            
            System.out.println(-ans);
        }
    }
}