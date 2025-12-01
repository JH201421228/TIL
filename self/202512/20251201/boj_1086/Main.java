package boj_1086;


import java.io.*;
import java.util.*;


public class Main {
    
    static int N, K;
    static int[] seq, pow_seq;
    static int[][] next_seq;
    static long[][] dp;
    static String[] string_seq;


    static long gcd(long a, long b) {
        while (b > 0) {
            long r = a % b;
            a = b;
            b = r;
        }

        return a;
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        string_seq = new String[N];
        for (int idx = 0; idx < N; ++idx) string_seq[idx] = br.readLine();
        K = Integer.parseInt(br.readLine());

        seq = new int[N];
        pow_seq = new int[N];
        next_seq = new int[N][K];
        dp = new long[1<<N][K];

        dp[0][0] = 1;

        for (int i = 0; i < N; ++i) {
            int cur = 0;
            String s = string_seq[i];

            for (int j = 0; j < s.length(); ++j) {
                cur = (cur * 10 + (s.charAt(j) - '0')) % K;
            }
            
            seq[i] = cur;

            int pow = 1;
            int len = string_seq[i].length();

            for (int j = 0; j < len; ++j) {
                pow = (pow * 10) % K;
            }

            pow_seq[i] = pow;
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < K; ++j) {
                next_seq[i][j] = (j * pow_seq[i] + seq[i]) % K;
            }
        }

        for (int cur = 0; cur < (1<<N); ++cur) {
            for (int i = 0; i < N; ++i) {
                if ((cur & (1<<i)) > 0) continue;

                for (int j = 0; j < K; ++j) {
                    dp[cur | (1<<i)][next_seq[i][j]] += dp[cur][j];
                }
            }
        }

        long a = dp[(1<<N)-1][0];
        long b = 0;
        for (int idx = 0; idx < K; ++idx) b += dp[(1<<N)-1][idx];

        long c = gcd(b, a);

        System.out.println(a/c + "/" + b/c);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}