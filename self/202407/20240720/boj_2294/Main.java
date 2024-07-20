import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NK = br.readLine().split(" ");

        int N = Integer.parseInt(NK[0]), K = Integer.parseInt(NK[1]);
        int[] dp = new int[K+1];

        int c;
        for (int i = 0; i < N; ++i) {
            c = Integer.parseInt(br.readLine());

            if (c <= K) {
                dp[c] = 1;

                for (int j = c+1; j < K+1; ++j) {
                    if (dp[j-c] != 0) {
                        if (dp[j] != 0) {
                            dp[j] = Math.min(dp[j], dp[j-c]+1);
                        }
                        else {
                            dp[j] = dp[j-c]+1;
                        }
                    }
                }
            }
        }

        if (dp[K] != 0) {
            System.out.println(dp[K]);
        }
        else {
            System.out.println(-1);
        }
    }
}