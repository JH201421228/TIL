import java.io.*;
import java.util.*;

public class Main {
    static int N, Q;
    static long[] arr;
    static List<Long> T[];

    static List<Long> merge(List<Long> X, List<Long> Y) {
        List<Long> res = new ArrayList<Long>();
        int i = 0, j = 0, x = X.size(), y = Y.size();

        while (i < x && j < y) {
            if (X.get(i) > Y.get(j)) {
                res.add(Y.get(j++));
            }
            else {
                res.add(X.get(i++));
            }
        }

        while (i < x) res.add(X.get(i++));
        while (j < y) res.add(Y.get(j++));

        return res;
    }

    static List<Long> I(int s, int e, int idx) {
        if (s == e) {
            T[idx].add(arr[s]);
            return T[idx];
        }

        int mid = (s+e) >> 1;

        T[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));
        return T[idx];
    }

    static int count(List<Long> X, long v) {
        int s = 0, e = X.size()-1;

        while (s <= e) {
            int mid = (s+e) >> 1;

            if (X.get(mid) < v) {
                s = mid+1;
            }
            else {
                e = mid-1;
            }
        }

        return s;
    }

    static int S(int s, int e, int idx, int l, int r, long v) {
        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return count(T[idx], v);
        }

        int mid = (s+e) >> 1;

        return S(s, mid, idx<<1, l, r, v) + S(mid+1, e, idx<<1|1, l, r, v);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NQ = br.readLine().split(" ");

        N = Integer.parseInt(NQ[0]);
        Q = Integer.parseInt(NQ[1]);

        T = new ArrayList[4*N+1];
        for (int i = 0; i < 4*N+1; ++i) {
            T[i] = new ArrayList<Long>();
        }

        arr = new long[N+1];
        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {
            arr[i+1] = Integer.parseInt(temp[i]);
        }

        I(1, N, 1);

        for (int i = 0; i < Q; ++i) {
            String[] tmp = br.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]), b = Integer.parseInt(tmp[1]); long c = Long.parseLong(tmp[2]);

            long s = -1_000_000_000, e = 1_000_000_000;

            while (s <= e) {
                long mid = (s+e) >> 1;

                if (S(1, N, 1, a, b, mid) < c) {
                    s = mid+1;
                }
                else {
                    e = mid-1;
                }
            }

            System.out.println(e);
        }
    }
}