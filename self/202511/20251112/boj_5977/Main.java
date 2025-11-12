package boj_5977;

import java.io.*;
import java.util.*;


public class Main {
    static int N, K;
    static int[] E;
    static long[] dp, sums;
    static Deque<Integer> q;

    static long temp(int idx) {
        return dp[idx-1] - sums[idx];
    }

    static void solve() {
        for (int idx = 1; idx < N+1; ++idx) sums[idx] = sums[idx-1] + E[idx];

        for (int idx = 1; idx < N+1; ++idx) {
            while (!q.isEmpty() && q.peekFirst() < idx-K) q.pollFirst();

            while (!q.isEmpty() && temp(q.peekLast()) <= temp(idx)) q.pollLast();

            q.add(idx);

            dp[idx] = sums[idx] + temp(q.peekFirst());

            if (idx <= K) dp[idx] = Math.max(dp[idx], sums[idx]);
        }

        System.out.println(dp[N]);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]);
        K = Integer.parseInt(NK[1]);

        E = new int[N+1];
        dp = new long[N+1];
        sums = new long[N+1];
        q = new ArrayDeque<Integer>();

        for (int idx = 1; idx < N+1; ++idx) E[idx] = Integer.parseInt(br.readLine());

        solve();
    }    
}
