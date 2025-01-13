import java.io.*;
import java.util.*;

public class Main {
    static int O, cnt, N, M;

    static int[] V, F, Vt, Vc;
    static List<Integer>[] G;

    static List<Integer> ans_list;

    static Stack<Integer> S;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) {
                p = Math.min(p, scc(x));
            }
            else if (F[x] == 0) {
                p = Math.min(p, V[x]);
            }
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

    static boolean dfs(int n, int flag) {
        Vt[n] = 1;

        for (int x : G[n]) {
            if (Vt[x] == 0) {
                if (F[x] != flag) return false;

                if (!dfs(x, flag)) return false;
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] NM = br.readLine().split(" ");
            N = Integer.parseInt(NM[0]); if (N == 0) break; M = Integer.parseInt(NM[1]);

            V = new int[N+1]; F = new int[N+1]; Vc = new int[N+1];
            G = new ArrayList[N+1];
            for (int i = 0; i < N+1; ++i) {
                G[i] = new ArrayList<Integer>();
            }

            String[] temp = br.readLine().split(" ");
            for (int i = 0; i < M; ++i) {
                int u, v; u = Integer.parseInt(temp[2*i]); v = Integer.parseInt(temp[2*i+1]);
                G[u].add(v);
            }

            O = 0; cnt = 0; S = new Stack<Integer>();
            for (int n = 1; n < N+1; ++n) {
                if (V[n] == 0) {
                    scc(n);
                }
            }

            ans_list = new ArrayList<Integer>();
            for (int n = 1; n < N+1; ++n) {
                if (Vc[F[n]] == 0) {
                    Vc[F[n]] = 1;
                    Vt = new int[N+1];
                    if (dfs(n, F[n])) ans_list.add(F[n]);
                }
            }

            for (int i = 1; i < N+1; ++i) {
                if (ans_list.contains(F[i])) {
                    System.out.print(i);
                    System.out.print(" ");
                };
            }
            System.out.println();
        }
    }
}