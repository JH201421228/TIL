package boj_13977;


import java.io.*;
import java.util.*;


class Main {
    static long MOD = 1_000_000_007;
    static long[] mods = new long[4_000_001];
    static int T, N, K;
    

    static long binary_exponentiation(long n) {
        long res = 1;
        long p = MOD - 2;

        while (p > 0) {
            if (p%2 > 0) res = (res * n) % MOD;
            p /= 2;
            n *= n;
            n %= MOD;
        }

        return res;
    }


    static void solve(BufferedReader br) throws IOException {
        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]);
        K = Integer.parseInt(NK[1]);

        System.out.println((mods[N] * binary_exponentiation(mods[K] * mods[N-K] % MOD)) % MOD);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        mods[0] = 1; mods[1] = 1;

        for (int i = 2; i < 4_000_001; ++i) mods[i] = (mods[i-1] * i) % MOD;

        T = Integer.parseInt(br.readLine());

        while (T-- > 0) solve(br);

        return;
    }
}