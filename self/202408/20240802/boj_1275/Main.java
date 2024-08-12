import java.util.*;
import java.io.*;

public class Main {
    static long[] nums;
    static long[] tree;

    public static long I(int s, int e, int idx) {
        if (s == e) {
            tree[idx] = nums[s];
            return tree[idx];
        }

        int mid = (s+e) / 2;
        tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1);
        return tree[idx];
    }

    public static long S(int s, int e, int l, int r, int idx) {
        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[idx];
        }

        int mid = (s+e) / 2;
        long val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1);
        return val;
    }

    public static void U(int s, int e, int nums_idx, int tree_idx, long v) {
        if (nums_idx > e || nums_idx < s) {
            return;
        }

        tree[tree_idx] += v;

        if (s == e) {
            return;
        }

        int mid = (s+e) / 2;
        U(s, mid, nums_idx, tree_idx*2, v);
        U(mid+1, e, nums_idx, tree_idx*2+1, v);
        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NQ = br.readLine().split(" ");
        int N = Integer.parseInt(NQ[0]), Q = Integer.parseInt(NQ[1]);

        nums = new long[N+1];
        tree = new long[4*N];
        nums[0] = 0;

        String[] input = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {
            nums[i+1] = Long.parseLong(input[i]);
        }

        I(1, N, 1);

        for (int i = 0; i < Q; ++i) {
            input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]), y = Integer.parseInt(input[1]), a = Integer.parseInt(input[2]);
            long b = Long.parseLong(input[3]);
            System.out.println(S(1, N, Math.min(x, y), Math.max(x, y), 1));
            U(1, N, a, 1, b-nums[a]);
            nums[a] = b;
        }

        return;
    }
}