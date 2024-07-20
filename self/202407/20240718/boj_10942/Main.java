package boj_10942;

import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            nums[i] = Integer.parseInt(input[i]);
        }

        int M = Integer.parseInt(br.readLine());

        int[][] dp = new int[N][N];
        int di = -1, dj = 1;
        int n;

        for (int i = 0; i < N; ++i) {
            dp[i][i] = 1;
            if (i+1 < N && nums[i] == nums[i+1]) {
                dp[i][i+1] = 1;
            }

            n = 1;
            while (i+n*di >= 0 && i+n*dj < N) {
                if (dp[i+(n-1)*di][i+(n-1)*dj] == 0) {
                    break;
                }
                else if (nums[i+n*di] == nums[i+n*dj]) {
                    dp[i+n*di][i+n*dj] = 1;
                }
                ++n;
            }

            n = 1;
            while (i+n*di >= 0 && i+n*dj+1 < N) {
                if (dp[i+(n-1)*di][i+(n-1)*dj+1] == 0) {
                    break;
                }
                else if (nums[i+n*di] == nums[i+n*dj+1]) {
                    dp[i+n*di][i+n*dj+1] = 1;
                }
                ++n;
            }
        }

        for (int i = 0; i < M; ++i) {
            String[] se = br.readLine().split(" ");
            int S = Integer.parseInt(se[0]);
            int E = Integer.parseInt(se[1]);

            bw.write(dp[S - 1][E - 1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }    
}
