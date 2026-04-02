import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] cur = new int[10_000];
    static int[] tar = new int[10_000];
    static int[][] dp = new int[10_001][10];
    static int[][] trace = new int[10_001][10];

    static Stack<Integer> ans = new Stack<>();

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N+1; ++i) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
            Arrays.fill(trace[i], 0);
        }

        for (int idx = 0; idx < 10; ++idx) dp[0][idx] = idx;

        String[] tmp1, tmp2; tmp1 = br.readLine().split(""); tmp2 = br.readLine().split("");

        for (int i = 0; i < N; ++i) cur[i] = Integer.parseInt(tmp1[i]);
        for (int i = 0; i < N; ++i) tar[i] = Integer.parseInt(tmp2[i]);

        for (int i = 1; i < N+1; ++i) {
            for (int j = 0; j < 10; ++j) {
                for (int k = 0; k < 10; ++k) {
                    int l = (j-k+10) % 10;
                    int cur_n = (cur[i-1] + j) % 10;
                    int diff = (cur_n - tar[i-1] + 10) % 10;

                    if (dp[i-1][k] + diff + l < dp[i][j]) {
                        dp[i][j] = dp[i-1][k] + diff + l;
                        trace[i][j] = k;
                    }
                }
            }
        }

        int min_val = dp[N][0];
        int cur_idx = 0;

        for (int i = 1; i < 10; ++i) {
            if (dp[N][i] < min_val) {
                min_val = dp[N][i];
                cur_idx = i;
            }
        }

        System.out.println(min_val);

        ans.push(cur_idx);
        for (int idx = N; idx > 1; --idx) {
            cur_idx = trace[idx][cur_idx];
            ans.push(cur_idx);
        }

        int acc = 0;
        int idx = 0;
        while (!ans.isEmpty()) {
            int a = ans.pop();
            int left = (a - acc + 10) % 10;
            int right = ((cur[idx] + a) % 10 - tar[idx] + 10) % 10;

            if (left > 0) System.out.println((idx+1) + " " + left);
            else System.out.println((idx+1) + " " + -right);

            acc = a; ++idx;
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}