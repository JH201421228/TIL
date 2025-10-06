package boj_15647;

import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] V, nodes;
    static long[] inner, outer;
    static List<int[]>[] G;

    static void set_inner(int n) {
        nodes[n] = 1;

        for (int[] xd : G[n]) {
            if (nodes[xd[0]] == 0) {
                set_inner(xd[0]);
                nodes[n] += nodes[xd[0]];
                inner[n] += inner[xd[0]] + nodes[xd[0]] * xd[1];
            }
        }

        return;
    }


    static void set_outer(int n) {
        V[n] = 1;

        for (int[] xd : G[n]) {
            int x = xd[0], d = xd[1];
            if (V[x] == 0) {
                outer[x] = outer[n] + (N - nodes[n]) * d + inner[n] - (inner[x] + nodes[x] * d) + (nodes[n] - nodes[x]) * d;
                set_outer(x);
            }
        }

        return;
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        V = new int[N+1];
        nodes = new int[N+1];
        inner = new long[N+1];
        outer = new long[N+1];
        G = new List[N+1];
        for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<int[]>();

        for (int i = 0; i < N-1; ++i) {
            String[] uvd = br.readLine().split(" ");
            int u = Integer.parseInt(uvd[0]);
            int v = Integer.parseInt(uvd[1]);
            int d = Integer.parseInt(uvd[2]);

            G[u].add(new int[] {v, d});
            G[v].add(new int[] {u, d});
        }

        set_inner(1);
        set_outer(1);

        for (int i = 1; i < N+1; ++i) {
            System.out.println(inner[i] + outer[i]);
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}