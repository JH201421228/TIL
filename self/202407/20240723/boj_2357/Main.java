import java.io.*;
import java.util.*;


public class Main {
    static long[] nums, tree1, tree2;

    static long MAX = 1000000000;

    static long I1(int s, int e, int idx) {
        if (s >= e) {
            tree1[idx] = nums[s];
            return tree1[idx];
        }

        int mid = (s+e) / 2;
        tree1[idx] = Math.min(I1(s, mid, idx*2), I1(mid+1, e, idx*2+1));
        return tree1[idx];
    }

    static long I2(int s, int e, int idx) {
        if (s >= e) {
            tree2[idx] = nums[s];
            return tree2[idx];
        }

        int mid = (s+e) / 2;
        tree2[idx] = Math.max(I2(s, mid, idx*2), I2(mid+1, e, idx*2+1));
        return tree2[idx];
    }


    static long S1(int s, int e, int l, int r, int idx) {
        if (s > r || e < l) {
            return MAX;
        }

        if (s >= l && e <= r) {
            return tree1[idx];
        }

        int mid = (s+e) / 2;
        long v = Math.min(S1(s, mid, l, r, idx*2), S1(mid+1, e, l, r, idx*2+1));
        return v;
    }


    static long S2(int s, int e, int l, int r, int idx) {
        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree2[idx];
        }

        int mid = (s+e) / 2;
        long v = Math.max(S2(s, mid, l, r, idx*2), S2(mid+1, e, l, r, idx*2+1));
        return v;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]), M = Integer.parseInt(NM[1]);

        nums = new long[N+1];
        tree1 = new long[4*N];
        tree2 = new long[4*N];

        for (int i = 0; i < N; ++i) {
            nums[i+1] = Long.parseLong(br.readLine());
        }

        I1(1, N, 1);
        I2(1, N, 1);

        for (int i = 0; i < M; ++i) {
            String[] ab = br.readLine().split(" ");
            int a = Integer.parseInt(ab[0]), b = Integer.parseInt(ab[1]);
            System.out.println(S1(1, N, a, b, 1) + " " + S2(1, N, a, b, 1));
        }
    }
}
