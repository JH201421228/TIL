import java.io.*;
import java.util.*;


public class Main {
    static int N, P, C[][], L[];
    static List<Integer> G[];
    
    static void set_edge(int u, int v) {
        G[u].add(v);
        G[v].add(u);
        C[u][v] = 1;
        C[v][u] = 0;
    }

    static boolean bfs(int src, int sink) {
        for (int i = 0; i < 2*N+1; ++i) L[i] = -1;
        Queue<Integer> q = new LinkedList<>();
        q.add(src);
        L[src] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();

            for (int v : G[u]) {
                if (L[v] == -1 && C[u][v] > 0) {
                    L[v] = L[u]+1;
                    q.add(v);
                }
            }
        }

        return L[sink] != -1;
    }

    static int dfs(int u, int sink) {
        if (u == sink) {
            return 1;
        }

        for (int v : G[u]) {
            if (L[v] == L[u]+1 && C[u][v] > 0) {
                int k = dfs(v, sink);
                if (k == 1) {
                    C[u][v] = 0;
                    C[v][u] = 1;
                    return k;
                }
            }
        }

        return 0;
    }

    static int max_flow(int src, int sink) {
        int ans = 0;
        
        while (bfs(src, sink)) {
            int flow = dfs(src, sink);
            if (flow == 0) {
                break;
            }
            ans += flow;
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NP = br.readLine().split(" ");
        N = Integer.parseInt(NP[0]); P = Integer.parseInt(NP[1]);
        C = new int[2*N+1][2*N+1];
        L = new int[2*N+1];

        G = new ArrayList[2*N+1];
        for (int i = 0; i < 2*N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }

        for (int i = 3; i < N+1; ++i) {
            set_edge(i, i+N);
        }

        for (int i = 0; i < P; ++i) {
            String[] temp = br.readLine().split(" ");
            int u = Integer.parseInt(temp[0]), v = Integer.parseInt(temp[1]);

            if (u > 2) {
                set_edge(u+N, v);
            }
            else {
                set_edge(u, v);
            }

            if (v > 2) {
                set_edge(v+N, u);
            }
            else {
                set_edge(v, u);
            }
        }

        System.out.println(max_flow(1, 2));
    }
}