import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] T = new int[2000001 * 4 + 1];

    static int U(int s, int e, int idx, int v) {
        if (s == e && s == v) {
            ++T[idx];
            return T[idx];
        }

        if (s > v || e < v) {
            return T[idx];
        }

        int mid = (s+e) >> 1;

        T[idx] = U(s, mid, idx<<1, v) + U(mid+1, e, idx<<1|1, v);

        return T[idx];
    }

    static int D(int s, int e, int idx, int v) {
        if (s == e) {
            --T[idx];
            return s;
        }

        int mid = (s+e) >> 1;
        int res;

        if (T[idx<<1] >= v) {
            res = D(s, mid, idx<<1, v);
        }
        else {
            res = D(mid+1, e, idx<<1|1, v-T[idx<<1]);
        }
        
        --T[idx];

        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] tx = br.readLine().split(" ");
            int t = Integer.parseInt(tx[0]), x = Integer.parseInt(tx[1]);

            if (t == 1) {
                U(1, 2000000, 1, x);
            }
            else {
                System.out.println(D(1, 2000000, 1, x));
            }
        }
    }
}