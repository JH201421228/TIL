import java.io.*;
import java.util.*;


public class Main {
    static int[] A;
    static int[] E;
    static int cnt = 0;
    static List<Integer>[] G;
    static int[] T;

    static void dfs(int n) {
        A[n] = ++cnt;
        for (int x : G[n]) {
            dfs(x);
        }
        E[n] = cnt;
    }

    static void U(int idx, int v, int N) {
        while (idx < N+1) {
            T[idx] += v;
            idx += (idx & -idx);
        }
    }

    static int S(int idx) {
        int res = 0;
        while (idx > 0) {
            res += T[idx];
            idx -= (idx & -idx);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]), M = Integer.parseInt(NM[1]);

        A = new int[N+1];
        E = new int[N+1];
        T = new int[N+1];
        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }

        String[] temp = br.readLine().split(" ");
        for (int i = 1; i < N; ++i) {
            G[Integer.parseInt(temp[i])].add(i+1);
        }

        dfs(1);

        for (int i = 0; i < M; ++i) {
            String[] tmp = br.readLine().split(" ");

            if (Integer.parseInt(tmp[0]) == 1) {
                U(A[Integer.parseInt(tmp[1])], Integer.parseInt(tmp[2]), N);
            }
            else {
                System.out.println(S(E[Integer.parseInt(tmp[1])]) - S(A[Integer.parseInt(tmp[1])]-1));
            }
        }
    }
}