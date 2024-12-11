import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
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

    static int count(List<Long> X, long k) {
        int s = 0, e = X.size()-1;

        while (s <= e) {
            int mid = (s+e) >> 1;

            if (X.get(mid) > k) {
                e = mid-1;
            }
            else {
                s = mid+1;
            }
        }

        return X.size()-s;
    }

    static int S(int s, int e, int idx, int l, int r, long k) {
        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return count(T[idx], k);
        }

        int mid = (s+e) >> 1;
        
        return S(s, mid, idx<<1, l, r, k) + S(mid+1, e, idx<<1|1, l, r, k);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new long[N+1];
        T = new ArrayList[4*N+1];
        for (int i = 0; i < 4*N+1; ++i) {
            T[i] = new ArrayList<Long>();
        }

        String[] temp = br.readLine().split(" ");
        for (int i = 1; i < N+1; ++i) {
            arr[i] = Integer.parseInt(temp[i-1]);
        }

        I(1, N, 1);

        M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] tmp = br.readLine().split(" ");
            System.out.println(S(1, N, 1, Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1]), Long.parseLong(tmp[2])));
        }
    }
}