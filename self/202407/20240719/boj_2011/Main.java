import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String S = br.readLine();
        int s = S.length();

        int[] dp = new int[s];
        dp[0] = 1;

        if (S.charAt(0) == '0') {
            System.out.println(0);
            return;
        }

        if (s >= 2) {
            if (S.charAt(1) == '0') {
                if (S.charAt(0) == '1' || S.charAt(0) == '2') {
                    dp[1] = dp[0];
                }
                else {
                    System.out.println(0);
                    return;
                }
            }
            else {
                dp[1] = 1;
                if ((S.charAt(0) - '0') * 10 + (S.charAt(1) - '0') <= 26) {
                    dp[1] = 2;
                }
            }
        }
    
        for (int i = 2; i < s; ++i) {
            if (S.charAt(i) == '0') {
                if (S.charAt(i-1) == '1' || S.charAt(i-1) == '2') {
                    dp[i] = dp[i-2];
                }
                else {
                    System.out.println(0);
                    return;
                }
            }
            else {
                dp[i] = dp[i-1];
                if (S.charAt(i-1) == '0') {
                    continue;
                }
                else if ((S.charAt(i-1) - '0') * 10 + (S.charAt(i) - '0') <= 26) {
                    dp[i] += dp[i-2];
                    dp[i] %= 1000000;
                }
            }
        }

        System.out.println(dp[s-1]);
    }
}
