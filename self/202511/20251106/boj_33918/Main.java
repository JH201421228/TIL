package boj_33918;

import java.io.*;
import java.util.*;


public class Main {
    static int N, M, C, D, ans = Integer.MIN_VALUE;
    static int[] B;
    static int[][] dp;
    static Queue<int[]> pq;

    static void solve() {
        for (int time = 0; time < N; ++time) {
            for (int temp = 1; temp < M+1; ++temp) {
                dp[time][temp] = M - Math.abs(temp - B[time]);
            }
        }

        for (int time = 0; time < N-1; ++time) {
            for (int offset = 1; offset < C+1; ++offset) {
                while (!pq.isEmpty()) pq.poll();

                for (int temp = offset; temp < Math.min(offset+D, M)+1; temp += C) pq.add(new int[] {dp[time][temp], temp});

                for (int temp = offset; temp < M+1; temp += C) {
                    if (temp != offset && temp+D < M+1) pq.add(new int[] {dp[time][temp+D], temp+D});

                    while (!pq.isEmpty() && pq.peek()[1] + D < temp) pq.poll();

                    dp[time+1][temp] += pq.peek()[0];
                }
            }
        }

        for (int idx = 0; idx < M+1; ++idx) ans = Math.max(ans, dp[N-1][idx]);

        System.out.println(ans);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NMCD = br.readLine().split(" ");
        N = Integer.parseInt(NMCD[0]);
        M = Integer.parseInt(NMCD[1]);
        C = Integer.parseInt(NMCD[2]);
        D = Integer.parseInt(NMCD[3]);

        B = new int[N];
        dp = new int[N][M+1];
        pq = new PriorityQueue<int[]>((a, b) -> Integer.compare(b[0], a[0]));

        String[] B_string = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) B[idx] = Integer.parseInt(B_string[idx]);

        solve();

        return;
    }
}