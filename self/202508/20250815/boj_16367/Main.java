import java.io.*;
import java.util.*;

public class Main {
    static int K, N, O = 0, cnt = 0;
    static int[] V, F;
    static Stack<Integer> S;
    static List<Integer>[] G;

    static Map<String, Integer> color = new HashMap<>();
    static {color.put("R", 0); color.put("B", 1);}

    static void minor_setting(int a, int b, int c, int d) {
        G[b].add(a);
        G[c].add(d);

        return;
    }

    static void setting(int a, String b, int c, String d, int e, String f) {
        minor_setting(2*a+color.get(b), 2*c+1-color.get(d), 2*a+1-color.get(b), 2*c+color.get(d));
        minor_setting(2*a+color.get(b), 2*e+1-color.get(f), 2*a+1-color.get(b), 2*e+color.get(f));
        minor_setting(2*c+color.get(d), 2*e+1-color.get(f), 2*c+1-color.get(d), 2*e+color.get(f));

        return;
    }

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

            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = cnt;

                if (o == n) break;
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] KN = br.readLine().split(" ");
        N = Integer.parseInt(KN[1]); K = Integer.parseInt(KN[0]);

        G = new List[2*K+2];
        for (int idx = 0; idx < 2*K+2; ++idx) G[idx] = new ArrayList<Integer>();

        V = new int[2*K+2];
        F = new int[2*K+2];

        S = new Stack<Integer>();

        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            setting(Integer.parseInt(temp[0]), temp[1], Integer.parseInt(temp[2]), temp[3], Integer.parseInt(temp[4]), temp[5]);
        }

        for (int n = 2; n < 2*K+2; ++n) {
            if (V[n] == 0) scc(n);
        }

        String ans = "";

        for (int n = 1; n < K+1; ++n) {
            if (F[2*n] == F[2*n+1]) {
                System.out.println(-1);
                return;
            }
            else if (F[2*n] < F[2*n+1]) ans += "R";
            else ans += "B";
        }

        System.out.println(ans);

        return;
    }
}
