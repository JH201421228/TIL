import java.io.*;
import java.util.*;


public class Main {
    static int MAX = 1_000_000_000;
    static int T, K, C;

    static long[] egcd(long a, long b) {
        long x0 = 1;
        long x1 = 0;
        long y0 = 0;
        long y1 = 1;

        long na, nb, nx0, nx1, ny0, ny1;

        while (b != 0) {
            long q = a / b;
            na = b; nb = a % b; a = na; b = nb;
            nx0 = x1; nx1 = x0 - q*x1; x0 = nx0; x1 = nx1;
            ny0 = y1; ny1 = y0 - q*y1; y0 = ny0; y1 = ny1;
        }

        return new long[] {a, x0, y0};
    }
    

    static void solve(BufferedReader br) throws IOException {
        String[] KC = br.readLine().split(" ");
        K = Integer.parseInt(KC[0]);
        C = Integer.parseInt(KC[1]);

        if (C == 1) {
            if (K+1 <= MAX) System.out.println(K+1);
            else System.out.println("IMPOSSIBLE");
            return;
        }

        if (K == 1) {
            System.out.println(1);
            return;
        }

        long[] temp  = egcd((long) C, (long) K);

        if (temp[0] != 1) {
            System.out.println("IMPOSSIBLE");
            return;
        }

        long ans = (temp[1] % K + K) % K;

        if (ans == 0) ans += K;

        if (ans > MAX) {
            System.out.println("IMPOSSIBLE");
            return;
        }

        System.out.println(ans);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) solve(br);

        return;
    }    
}
