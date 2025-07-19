package boj_26157;

import java.util.*;
import java.io.*;

public class Main {
    static int N, M, O = 0, Z = 0, cmp = 1;
    static int[] F, V, order;
    static List<Integer> ans;
    static List<Integer>[] G, graph;
    static Stack<Integer> S;
    static Queue<Integer> q;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            ++Z;

            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = Z;

                if (n == o) break;
            }
        }

        return p;
    }

    static void generate_graph() {
        for (int n = 1; n < N+1; ++n) {
            int u = F[n];

            for (int x : G[n]) {
                int v = F[x];

                if (u == v) continue;

                graph[u].add(v);
                ++order[v];
            }
        }

        return;
    }

    static void topology_sort() {
        for (int idx = 1; idx < Z+1; ++idx) {
            if (order[idx] == 0) q.offer(idx);
        }

        if (q.size() > 1) {
            System.out.println(0);
            return;
        }

        int res = q.peek();
        while (!q.isEmpty()) {
            if (q.size() > 1) {
                System.out.println(0);
                return;
            }

            int n = q.poll();
            for (int x : graph[n]) {
                --order[x];

                if (order[x] == 0) {
                    q.offer(x);
                    ++cmp;
                }
            }
        }

        if (cmp == Z) {
            for (int idx = 1; idx < N+1; ++idx) {
                if (F[idx] == res) ans.add(idx);
            }

            System.out.println(ans.size());
            for (int x : ans) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }
        else {
            System.out.println(0);
            return;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        F = new int[N+1]; V = new int[N+1]; order = new int[N+1];
        ans = new ArrayList<Integer>();
        G = new List[N+1]; graph = new List[N+1];
        for (int idx = 0; idx < N+1; ++idx) {
            G[idx] = new ArrayList<Integer>();
            graph[idx] = new ArrayList<Integer>();
        }
        S = new Stack<Integer>();
        q = new LinkedList<Integer>();

        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]); int v = Integer.parseInt(uv[1]);
            G[u].add(v);
        }

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        generate_graph();

        topology_sort();

        return;
    }
}
