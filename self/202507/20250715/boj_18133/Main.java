import java.io.*;
import java.util.*;

public class Main {
    static int N, M, O = 0, cnt = 0;
    static int[] V, F;
    static List<Integer>[] G;
    static Stack<Integer> S;
    static Map<Integer, List<Integer>> connection;
    static Set<Integer> uniques;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            ++cnt;

            while (!S.empty()) {
                int o = S.pop();
                F[o] = cnt;

                if (o == n) break;
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        V = new int[N+1]; F = new int[N+1];
        S = new Stack<Integer>();
        G = new List[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<Integer>();
        connection = new HashMap<Integer, List<Integer>>();
        uniques = new HashSet<>();

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]); int v = Integer.parseInt(uv[1]);
            G[u].add(v);
        }

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        for (int idx = 1; idx < N+1; ++idx) {
            uniques.add(F[idx]);
        }

        for (int n : uniques) connection.put(n, new ArrayList<Integer>());

        for (int n = 1; n < N+1; ++n) {
            for (int x : G[n]) {
                if (F[x] != F[n]) connection.get(F[x]).add(F[n]);
            }
        }

        int ans = 0;
        for (Map.Entry<Integer, List<Integer>> entry : connection.entrySet()) {
            if (entry.getValue().isEmpty()) ++ans;
        };

        System.out.println(ans);
    }
}
