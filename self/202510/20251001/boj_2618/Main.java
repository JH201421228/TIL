package boj_2618;

import java.io.*;
import java.util.*;


public class Main {
    static int N, W;
    static int[][] dp = new int[1_003][1_003];
    static int[][] dp_trace = new int[1_003][1_003];
    static int[][] tasks = new int[1_003][2];

    static int dist(int i, int j) {
        return Math.abs(tasks[i][0] - tasks[j][0]) + Math.abs(tasks[i][1] - tasks[j][1]);
    }

    static int cal(int n, int m) {
        int x = Math.max(n, m) + 1;
        
        if (x == W+2) return 0;
        if (dp[n][m] != -1) return dp[n][m];

        int first = cal(n, x) + dist(m, x);
        int second = cal(x, m) + dist(n, x);

        if (first > second) {
            dp[n][m] = second;
            dp_trace[n][m] = 1;
        }
        else {
            dp[n][m] = first;
            dp_trace[n][m] = 2;
        }

        return dp[n][m];
    }

    static void solve(int N, int W, BufferedReader br) throws IOException {
        tasks[0][0] = 1; tasks[0][1] = 1;
        tasks[1][0] = N; tasks[1][1] = N;

        for (int i = 0; i < W; ++i) {
            String[] temp = br.readLine().split(" "); int a = Integer.parseInt(temp[0]); int b = Integer.parseInt(temp[1]);
            tasks[i+2][0] = a; tasks[i+2][1] = b;
        }

        for (int i = 0; i < dp.length; ++i) {
            Arrays.fill(dp_trace[i], -1); Arrays.fill(dp[i], -1);
        }

        System.out.println(cal(0, 1));

        int n = 0, m = 1;
        for (int i = 2; i < W+2; ++i) {
            System.out.println(dp_trace[n][m]);
            if (dp_trace[n][m] == 1) {
                n = i;
            }
            else {
                m = i;
            }
        }

        return;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        W = Integer.parseInt(br.readLine());

        solve(N, W, br);

        return;
    }    
}
