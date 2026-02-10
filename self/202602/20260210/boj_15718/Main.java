package boj_15718;


import java.io.*;
import java.util.*;


class Main {
    static int MOD = 100_007;
    static int N, M, T;
    static int fac1[] = new int[97];
    static int fac2[] = new int[1031];
    static int inv1[] = new int[97];
    static int inv2[] = new int[1031];


    static int lucas(int n, int k, int[] fac, int[] inv, int p) {
        int res = 1;
        int a, b;

        while (n > 0 || k > 0) {
            a = n % p; b = k % p;

            if (b > a) return 0;

            res = res * ((fac[a] * inv[b] % p) * inv[a-b] % p) % p;

            n /= p; k /= p;
        }

        return res;
    }


    static int egcd(int a, int b) {
        int x0 = 1, x1 = 0, y0 = 0, y1 = 1, p = a;

        while (b > 0) {
            int q = a / b;
            int a_ = b, b_ = a % b;
            int x0_ = x1, x1_ = x0 - q * x1;
            int y0_ = y1, y1_ = y0 - q * y1;

            a = a_; b = b_; x0 = x0_; x1 = x1_; y0 = y0_; y1 = y1_; 
        }

        if (y0 < 0) y0 += p;

        return y0;
    }


    static int crt(int a, int b) {
        int res = 0;

        res = (res + (a * 1031 % MOD) * egcd(97, 1031) % MOD) % MOD;
        res = (res + (b * 97 % MOD) * egcd(1031, 97) % MOD) % MOD;

        return res;
    }


    static void solve(BufferedReader br) throws IOException {
        String[] NM = br.readLine().split(" ");
        N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        if (N == 0 && M == 1) {
            System.out.println(1);
            return;
        }

        if (N == 0) {
            System.out.println(0);
            return;
        }

        if (M == 1) {
            System.out.println(0);
            return;
        }

        int a = lucas(N-1, M-2, fac1, inv1, 97);
        int b = lucas(N-1, M-2, fac2, inv2, 1031);

        System.out.println(crt(a, b));

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        fac1[0] = 1; fac1[1] = 1; fac2[0] = 1; fac2[1] = 1;

        for (int i = 1; i < 97; ++i) fac1[i] = fac1[i-1] * i % 97;
        for (int i = 1; i < 1031; ++i) fac2[i] = fac2[i-1] * i % 1031;

        inv1[96] = egcd(97, fac1[96]);
        inv2[1030] = egcd(1031, fac2[1030]);

        for (int i = 96; i > 0; --i) inv1[i-1] = inv1[i] * i % 97;
        for (int i = 1030; i > 0; --i) inv2[i-1] = inv2[i] * i % 1031;

        T = Integer.parseInt(br.readLine());

        while (T-- > 0) solve(br);

        return;
    }

}