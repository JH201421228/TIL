import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int T = Integer.parseInt(input[0]), W = Integer.parseInt(input[1]), prev = 0, cnt = 0;
        List<Integer> vals = new ArrayList<>();

        for (int i = 0; i < T; i++) {
            int v = Integer.parseInt(br.readLine());

            if (i == 0 && v == 1) {
                vals.add(0);
            }

            if (prev != 0 && prev != v) {
                vals.add(cnt);
                cnt = 0;
            }

            ++cnt;
            prev = v;
        }
        vals.add(cnt);

        int L = vals.size() + 1;
        int[][] dp = new int[W+1][L];

        for (int i = 1; i < L; i++) {
            if (i%2 == 1) {
                dp[0][i] = dp[0][i-1];
            }
            else {
                dp[0][i] = dp[0][i-1] + vals.get(i-1);
            }
        }

        int ans = dp[0][L-1];

        for (int i = 1; i < W+1; i++) {
            for (int j = 1; j < L; j++) {
                if (i%2 == 1) {
                    if (j%2 == 1) {
                        dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]) + vals.get(j-1);
                    }
                    else {
                        dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]);
                    }
                }
                else {
                    if (j%2 == 1) {
                        dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]);
                    }
                    else {
                        dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]) + vals.get(j-1);
                    }
                }
            }

            ans = Math.max(ans, dp[i][L-1]);
        }

        System.out.println(ans);
    }
}
