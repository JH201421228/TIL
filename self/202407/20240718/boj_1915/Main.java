package boj_1915;

import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] nm = br.readLine().split(" ");
        int N, M, ans = 0;

        N = Integer.parseInt(nm[0]);
        M = Integer.parseInt(nm[1]);

        int[][] dp = new int[N][M];

        String S;

        for (int i = 0; i < N; ++i) {
            S = br.readLine();

            for (int j = 0; j < M; ++j) {
                dp[i][j] = S.charAt(j) - '0';
            }
        }

        for (int i = 0; i < N; ++i) {
            if (dp[i][0] == 1) {
                ans = 1;
                break;
            }
        }

        for (int i = 0; i < M; ++i) {
            if (dp[0][i] == 1) {
                ans = 1;
                break;
            }
        }

        for (int i = 1; i < N; ++i) {
            for (int j = 1; j < M; ++j) {
                if (dp[i][j] == 1) {
                    dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    ans = Math.max(ans, dp[i][j]);
                }
            }
        }

        System.out.println(ans*ans);
    }
}
