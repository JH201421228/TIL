import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T > 0) {
            --T;

            int N = Integer.parseInt(br.readLine());
            int[] coins = new int[N];
            String[] input = br.readLine().split(" ");

            for (int i = 0; i < N; ++i) {
                coins[i] = Integer.parseInt(input[i]);
            }

            int M = Integer.parseInt(br.readLine());
            int[] dp = new int[M+1];
            dp[0] = 1;

            for (int c: coins) {
                for (int i = c; i < M+1; ++i) {
                    dp[i] = dp[i] + dp[i-c];
                }
            }

            System.out.println(dp[M]);
        }
    }
}
