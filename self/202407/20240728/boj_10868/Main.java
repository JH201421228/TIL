import java.io.*;
import java.util.*;

public class Main {
    static long[] nums;
    static long[] st;
    static long MAXV = 1000000000;


    public static long I(int s, int e, int idx) {
        if (s == e) {
            st[idx] = nums[s];
            return st[idx];
        }

        int mid = (s+e) / 2;
        st[idx] = Math.min(I(s, mid, idx*2), I(mid+1, e, idx*2+1));
        return st[idx];
    }


    public static long S(int s, int e, int l, int r, int idx) {
        if (s > r || e < l) {
            return MAXV;
        }

        if (s >= l && e <= r) {
            return st[idx];
        }

        int mid = (s+e) / 2;
        long val = Math.min(S(s, mid, l, r, idx*2), S(mid+1, e, l, r, idx*2+1));
        return val;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]), M = Integer.parseInt(NM[1]);

        nums = new long[N+1];
        st = new long[4*N];
        Arrays.fill(st, MAXV);

        for (int i = 1; i <= N; ++i) {
            nums[i] = Long.parseLong(br.readLine());
        }

        I(1, N, 1);

        for (int i = 0; i < M; ++i) {
            String[] ab = br.readLine().split(" ");
            int a = Integer.parseInt(ab[0]), b = Integer.parseInt(ab[1]);
            System.out.println(S(1, N, a, b, 1));
        }
    }
}
