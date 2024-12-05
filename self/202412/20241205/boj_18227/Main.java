import java.io.*;
import java.util.*;

public class Main {
    static int N, C, M;
    static List<Integer> G[];
    static int[] A;
    static int[] E;
    static long[] T;
    static int[] W;
    static int cnt = 0;
    static int order = 0;

    static void dfs(int n) {
        A[n] = ++cnt;
        W[n] = ++order;
        for (int x : G[n]) {
            if (A[x] == 0) {
                dfs(x);
                --order;
            }
        }
        E[n] = cnt;
    }

    static void U(int idx) {
        while (idx < N+1) {
            T[idx] += 1;
            idx += (idx & -idx);
        }
    }

    static long S(int idx) {
        long res = 0;
        while (idx > 0) {
            res += T[idx];
            idx -= (idx & -idx);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NC = br.readLine().split(" ");
        N = Integer.parseInt(NC[0]);
        C = Integer.parseInt(NC[1]);

        A = new int[N+1];
        E = new int[N+1];
        T = new long[N+1];
        W = new int[N+1];

        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < N-1; ++i) {
            String[] temp = br.readLine().split(" ");
            G[Integer.parseInt(temp[0])].add(Integer.parseInt(temp[1]));
            G[Integer.parseInt(temp[1])].add(Integer.parseInt(temp[0]));
        }
        dfs(C);

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            if (Integer.parseInt(temp[0]) == 1) {
                U(A[Integer.parseInt(temp[1])]);
            }
            else {
                System.out.println(W[Integer.parseInt(temp[1])] * (S(E[Integer.parseInt(temp[1])]) - S(A[Integer.parseInt(temp[1])]-1)));
            }
        }
    }
}