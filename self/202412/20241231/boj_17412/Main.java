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

        return;
    }

    static boolean bfs(int src, int sink) {
        Arrays.fill(L, -1);
        L[src] = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(src);

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
                    return 1;
                }
            }
        }

        return 0;
    }

    static int get_ans(int src, int sink) {
        int ans = 0;

        while (bfs(src, sink)) {
            while (true) {
                int flow = dfs(src, sink);
                
                if (flow == 0) {
                    break;
                }

                ans += flow;
            }
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NP = br.readLine().split(" ");
        N = Integer.parseInt(NP[0]); P = Integer.parseInt(NP[1]);

        L = new int[N+1];
        C = new int[N+1][N+1];
        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < P; ++i) {
            String[] UV = br.readLine().split(" ");
            int u = Integer.parseInt(UV[0]), v = Integer.parseInt(UV[1]);
            set_edge(u, v);
        }

        System.out.println(get_ans(1, 2));
    }
}
