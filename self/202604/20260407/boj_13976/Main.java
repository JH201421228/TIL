package boj_13976;

import java.io.*;
import java.util.*;


public class Main {

    static long N;
    static long MOD = 1_000_000_007;

    static long[][] cal(long[][] mat1, long[][] mat2) {
        long[][] res = new long[2][2];

        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                for (int k = 0; k < 2; ++k) {
                    res[i][j] += (mat1[i][k] * mat2[k][j]) % MOD;
                    res[i][j] %= MOD;
                }
            }
        }

        return res;
    }

    static long[][] recur(long n, long[][] mat) {
        long[][] res = {{1, 0}, {0, 1}};

        while (n > 0) {
            if (n%2 > 0) res = cal(res, mat);
            mat = cal(mat, mat);
            n /= 2;
        }

        return res;
    }

    static void solve(BufferedReader br) throws IOException {
        N = Long.parseLong(br.readLine());

        if (N%2 > 0) {
            System.out.println(0);
            return;
        }

        long[][] res = {{4, -1}, {1, 0}};
        res = recur(N/2, res);
        System.out.println((res[0][0] + res[0][1] + MOD) % MOD);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    } 
}