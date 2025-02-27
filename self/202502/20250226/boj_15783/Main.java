import java.io.*;
import java.util.*;


public class Main {
    
    static int N, M, O = 0, ans = 0;
    static int[] V, F;
    static Stack<Integer> S = new Stack<Integer>();
    static List<Integer>[] G;
    static Map<Integer, Set<Integer>> checker;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            while (!S.empty()) {
                int o = S.pop();
                F[o] = p;
                if (o == n) break;
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        V = new int[N+1];
        F = new int[N+1];
        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) G[i] = new ArrayList<Integer>();

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]); int v = Integer.parseInt(uv[1]);
            G[u+1].add(v+1);
        }

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        checker = new HashMap<>();
        for (int i = 1; i < N+1; ++i) {
            checker.put(F[i], new HashSet<Integer>());
        }

        for (int s = 1; s < N+1; ++s) {
            for (int e : G[s]) {
                if (F[e] != F[s]) checker.get(F[e]).add(F[s]);
            }
        }

        for (Map.Entry<Integer, Set<Integer>> entry : checker.entrySet()) {
            if (entry.getValue().isEmpty()) ++ans;
        }

        System.out.println(ans);
    }    
}
