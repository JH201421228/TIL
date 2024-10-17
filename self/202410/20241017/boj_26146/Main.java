import java.util.*;
import java.io.*;


public class Main {
    static List<List<Integer>> G;
    static int[] V;
    static int[] F;
    static int O = 0;
    static ArrayList<Integer> S = new ArrayList<>();
    static int cnt = 0;

    static int scc(int n) {
        int p = V[n] = ++O;
        S.add(n);

        for (int x : G.get(n)) {
            if (V[x] == 0) {
                p = Math.min(p, scc(x));
            }
            else if (F[x] == 0) {
                p = Math.min(p, V[x]);
            }
        }

        if (p == V[n]) {
            ++cnt;

            while (!S.isEmpty()) {
                int out = S.remove(S.size()-1);
                F[out] = cnt;

                if (n == out) {
                    break;
                }
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]), M = Integer.parseInt(NM[1]);

        V = new int[N+1];
        F = new int[N+1];

        G = new ArrayList<>(N+1);
        for (int i = 0; i < N+1; ++i) {
            G.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" ");
            int u = Integer.parseInt(uv[0]), v = Integer.parseInt(uv[1]);

            G.get(u).add(v);
        }

        for (int i = 1; i < N+1; ++i) {
            if (V[i] == 0) {
                scc(i);
            }
        }

        if (cnt == 1) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}