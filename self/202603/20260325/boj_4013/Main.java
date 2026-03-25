package boj_4013;

import java.io.*;
import java.util.*;


public class Main {
    static int N, M, S, P, o = 0, group_n = 1;
    static int[] V, F, cash, restaurant, group_cash, group_restaurant, group_visit, indegree, dp;
    static List<Integer> G[], group_graph[];
    static Stack<Integer> sta, group_sta;
    static Queue<Integer> que;


    static int scc(int n) {
        ++o;
        int p = o;
        V[n] = o;
        sta.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            while (!sta.isEmpty()) {
                int c = sta.pop();
                F[c] = group_n;
                if (c == n) break;
            }
            ++group_n;
        }

        return p;
    }


    static void solve(BufferedReader br) throws IOException {
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);
        V = new int[N+1]; F = new int[N+1]; cash = new int[N+1]; restaurant = new int[N+1];
        G = new ArrayList[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<>();
        sta = new Stack<>(); group_sta = new Stack<>();
        que = new LinkedList<>();


        for (int i = 0; i < M; ++i) {
            String[] uv = br.readLine().split(" "); int u = Integer.parseInt(uv[0]); int v = Integer.parseInt(uv[1]);
            G[u].add(v);
        }

        for (int idx = 0; idx < N; ++idx) cash[idx+1] = Integer.parseInt(br.readLine());

        String[] SP = br.readLine().split(" "); S = Integer.parseInt(SP[0]); P = Integer.parseInt(SP[1]);

        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < P; ++i) restaurant[Integer.parseInt(temp[i])] = 1;

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        group_cash = new int[group_n]; group_restaurant = new int[group_n]; group_visit = new int[group_n]; indegree = new int[group_n]; dp = new int[group_n]; group_graph = new ArrayList[group_n]; for (int idx = 0; idx < group_n; ++idx) group_graph[idx] = new ArrayList<>();

        for (int n = 1; n < N+1; ++n) {
            int group = F[n];
            group_cash[group] += cash[n];
            if (restaurant[n] != 0) group_restaurant[group] = 1;

            for (int x : G[n]) {
                if (group != F[x]) group_graph[group].add(F[x]);
            }
        }

        S = F[S];
        group_visit[S] = 1;
        group_sta.push(S);

        while (!group_sta.isEmpty()) {
            int n = group_sta.pop();
            for (int x : group_graph[n]) {
                if (group_visit[x] == 0) {
                    group_visit[x] = 1;
                    group_sta.push(x);
                }
            }
        }

        for (int n = 1; n < group_n; ++n) {
            if (group_visit[n] == 0) continue;

            for (int x : group_graph[n]) {
                if (group_visit[x] != 0) ++indegree[x];
            }
        }

        dp[S] = group_cash[S];

        que.add(S);

        while (!que.isEmpty()) {
            int n = que.poll();

            for (int x : group_graph[n]) {
                dp[x] = Math.max(dp[x], dp[n] + group_cash[x]);

                --indegree[x];

                if (indegree[x] == 0) que.add(x);
            }
        }

        int ans = 0;

        for (int idx = 1; idx < group_n; ++idx) {
            if (group_restaurant[idx] != 0) ans = Math.max(ans, dp[idx]);
        }

        System.out.println(ans);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}