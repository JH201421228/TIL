import java.io.*;
import java.util.*;


public class Main {
    static int N, O = 0, C = 0;
    static int[] G, F, V;
    static Stack<Integer> S = new Stack<Integer>();
    static List<List<Integer>> L = new ArrayList<List<Integer>>();

    static int get_next(int n) {
        int res = n;
        while (n > 0) {
            res += n % 10;
            n /= 10;
        }

        return res;
    }

    static int scc(int n) {
        int p = ++O;
        V[n] = p;
        S.push(n);

        int x = G[n];
        if (V[x] == 0) p = Math.min(p, scc(x));
        else if (F[x] == 0) p = Math.min(p, V[x]);

        if (p == V[n]) {
            List<Integer> temp = new ArrayList<Integer>();

            while (!S.isEmpty()) {
                int o = S.pop();
                temp.add(o);
                F[o] = -1;

                if (o == n) {
                    L.add(temp);
                    break;
                }
            }
        }

        return p;
    }

    static int get_max_value(int n) {
        int x = G[n];

        if (x == n) F[n] = 1;
        else if (F[x] != 1) F[n] = F[x] + 1;
        else F[n] = get_max_value(x) + 1;

        return F[n];
    }

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        G = new int[N+1]; F = new int[N+1]; V = new int[N+1];

        for (int n = 1; n < N+1; ++n) {
            int x = get_next(n);
            if (x < N+1) G[n] = x;
            else if (x % N == 0) G[n] = N;
            else G[n] = x % N;
        }

        for (int n = 1; n < N+1; ++n) if (V[n] == 0) scc(n);

        for (List<Integer> temp : L) {
            int val = temp.size();

            for (int v : temp) F[v] = val;
        }

        for (int n = 1; n < N+1; ++n) {
            if (F[n] != 1) continue;
            get_max_value(n);
        }

        System.out.println(Arrays.stream(F).max().getAsInt());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        solve(br);
    }
}
