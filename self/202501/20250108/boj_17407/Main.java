import java.io.*;
import java.util.*;


public class Main {
    static int N, M, V, ans = 0;
    static int[] arr, T, L;
    static char[] S;

    static int I(int s, int e, int idx) {
        if (s == e) {
            T[idx] = arr[s];
            return arr[s];
        }

        int mid = (s+e) >> 1;

        T[idx] = Math.min(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));

        return T[idx];
    }

    static void lazy_U(int s, int e, int idx) {
        if (L[idx] != 0) {
            T[idx] += L[idx];
            if (s != e) {
                L[idx<<1] += L[idx];
                L[idx<<1|1] += L[idx];
            }
            L[idx] = 0;
        }
    }

    static int U(int s, int e, int idx, int l, int r, int v) {
        lazy_U(s, e, idx);

        if (s > r || e < l) {
            return T[idx];
        }

        if (s >= l && e <= r) {
            L[idx] += v;
            lazy_U(s, e, idx);
            return T[idx];
        }

        int mid = (s+e) >> 1;

        T[idx] = Math.min(U(s, mid, idx<<1, l, r, v), U(mid+1, e, idx<<1|1, l, r, v));
        
        return T[idx];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        S = br.readLine().toCharArray();
        M = Integer.parseInt(br.readLine());

        N = S.length;

        // for (String i : S) {
        //     System.out.println("test" + i);
        // }

        arr = new int[N+1];
        T = new int[4*N+1];
        L = new int[4*N+1];

        for (int i = 0; i < N; ++i) {
            if (S[i] == '(') {
                arr[i+1] = arr[i] + 1;
            }
            else {
                arr[i+1] = arr[i] - 1;
            }
        }

        V = arr[N];

        I(1, N, 1);

        for (int i = 0; i < M; ++i) {
            int q = Integer.parseInt(br.readLine());
            int k = 0;

            if (S[q-1] == '(') {
                S[q-1] = ')';
                V -= 2;
                k = U(1, N, 1, q, N, -2);
            }
            else {
                S[q-1] = '(';
                V += 2;
                k = U(1, N, 1, q, N, 2);
            }

            if (V == 0 && k >= 0) {
                ++ans;
            }
        }

        System.out.println(ans);
    }
}