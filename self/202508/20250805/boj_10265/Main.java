import java.io.*;
import java.util.*;

public class Main {
    static int N, K, O = 0, C = 0;
    static int[] V, F, U, dp, G;
    static List<Integer>[] cycle_parent, cycle_child;
    static Stack<Integer> S;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        int x = G[n];
        if (V[x] == 0) p = Math.min(p, scc(x));
        else if (F[x] == 0) p = Math.min(p, V[x]);

        if (p == V[n]) {
            ++C;

            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = C;
                U[C] += 1;

                if (o == n) break;
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]); K = Integer.parseInt(NK[1]);

        V = new int[N+1];
        F = new int[N+1];
        U = new int[N+1];
        dp = new int[N+1];
        G = new int[N+1];
        cycle_parent = new List[N+1]; for (int idx = 0; idx < N+1; ++idx) cycle_parent[idx] = new ArrayList<Integer>();
        cycle_child = new List[N+1]; for (int idx = 0; idx < N+1; ++idx) cycle_child[idx] = new ArrayList<Integer>();
        S = new Stack<Integer>();

        String[] temp = br.readLine().split(" ");
        for (int idx = 1; idx < N+1; ++idx) G[idx] = Integer.parseInt(temp[idx-1]);

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        for (int n = 1; n < N+1; ++n) {
            if (F[n] != F[G[n]]) {
                cycle_parent[F[G[n]]].add(F[n]);
                cycle_child[F[n]].add(F[G[n]]);
            }
        }

        dp[0] = 1;

        for (int x = 1; x < C+1; ++x) {
            if (cycle_child[x].isEmpty()) {
                List<Integer> tmp = new ArrayList<Integer>();
                Queue<Integer> q = new LinkedList<Integer>();
                q.offer(x);

                while (!q.isEmpty()) {
                    int n = q.poll();
                    tmp.add(n);

                    for (int nxt : cycle_parent[n]) {
                        q.offer(nxt);
                    }
                }

                int[] dp_temp = new int[N+1];
                for (int idx = 0; idx < N+1; ++idx) dp_temp[idx] = dp[idx];

                for (int n = U[tmp.get(0)]; n < U[tmp.get(0)] + tmp.size(); ++n) {
                    for (int idx = 0; idx < K; ++idx) {
                        if (dp[idx] != 0 && idx + n < K+1) dp_temp[idx + n] = 1;
                    }
                }

                for (int idx = 0; idx < N+1; ++idx) dp[idx] = dp_temp[idx];
            }
        }

        int ans = K;

        while (ans != 0) {
            if (dp[ans] != 0) break;

            --ans;
        }

        System.out.println(ans);

        return;
    }
}