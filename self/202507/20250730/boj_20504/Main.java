import java.io.*;
import java.util.*;

public class Main {
    static int N, M, O = 0, C = 0;
    static int[] V, F;
    static List<Integer>[] G;
    static Stack<Integer> S;
    static Map<Integer, Boolean> target_cycles;
    static Map<Integer, List<Integer>> parent;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            ++C;

            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = C;

                if (o == n) break;
            }
        }

        return p;
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        G = new List[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<Integer>();
        V = new int[N+1];
        F = new int[N+1];
        S = new Stack<Integer>();

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]); int v = Integer.parseInt(uv[1]);
            G[u].add(v);
        }

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        parent = new HashMap<>(); for (int idx = 1; idx < C+1; ++idx) parent.put(idx, new ArrayList<Integer>());
        target_cycles = new HashMap<>();

        for (int n = 1; n < N+1; ++n) {
            for (int x : G[n]) {
                if (F[n] != F[x]) parent.get(F[x]).add(F[n]);
            }
        }

        for (Map.Entry<Integer, List<Integer>> entry : parent.entrySet()) {
            Integer k = entry.getKey();
            List<Integer> v = entry.getValue();

            if (v.isEmpty()) target_cycles.put(k, false);
        }

        int Z = Integer.parseInt(br.readLine());
        for (int i = 0; i < Z; ++i) {
            int n = Integer.parseInt(br.readLine());
            if (target_cycles.containsKey(F[n])) target_cycles.put(F[n], true);
        }

        for (Map.Entry<Integer, Boolean> entry : target_cycles.entrySet()) {
            Boolean v = entry.getValue();
            if (!v) {
                System.out.println(-1);
                
                return;
            }
        }

        System.out.println(target_cycles.size());

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}
