import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] arg) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N+51];
        int ans = 0;

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            int d = Integer.parseInt(input[0]);
            int c = Integer.parseInt(input[1]);

            dp[i+d] = Math.max(dp[i+d], ans+c);
            ans = Math.max(dp[i+1], ans);
        }

        System.out.println(ans);
    }
}
