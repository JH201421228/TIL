import java.io.*;
import java.util.*;

public class Main {
    static int D, L, O = 0, ans = 0;
    static int[] V, F;
    static List<Integer>[] G;
    static Stack<Integer> S;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (V[n] == p) {
            int tmp = 0;

            while (!S.isEmpty()) {
                int o = S.pop();
                ++tmp;

                F[o] = 1;

                if (o == n) break;
            }

            ans = Math.max(ans, tmp);
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        D = Integer.parseInt(br.readLine());
        L = Integer.parseInt(br.readLine());

        G = new List[D+1]; for (int idx = 0; idx < D+1; ++idx) G[idx] = new ArrayList<Integer>();
        V = new int[D+1];
        F = new int[D+1];

        S = new Stack<Integer>();

        for (int i = 0; i < L; ++i) {
            String[] uv = br.readLine().split(" ");
            int u, v; u = Integer.parseInt(uv[0]); v = Integer.parseInt(uv[1]);

            G[u].add(v);
        }

        for (int n = 1; n < D+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        System.out.println(ans);
    }
}
