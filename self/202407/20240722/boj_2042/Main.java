import java.io.*;
import java.util.*;


public class Main {
    static long[] tree, nums;
    
    static long I(int s, int e, int idx) {
        if (s == e) {
            tree[idx] = nums[s-1];
            return tree[idx];
        }

        int mid = (s+e) / 2;
        tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1);
        return tree[idx];
    }

    static long S(int s, int e, int l, int r, int idx) {
        if (e < l || s > r) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[idx];
        }

        int mid = (s+e) / 2;
        long val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1);
        return val;
    }

    static void U(int s, int e, int idx, int cidx, long val) {
        if (cidx > e || cidx < s) {
            return;
        }

        tree[idx] += val;

        if (s == e) {
            return;
        }

        int mid = (s+e) / 2;
        U(s, mid, idx*2, cidx, val);
        U(mid+1, e, idx*2+1, cidx, val);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NMK = br.readLine().split(" ");
        int N = Integer.parseInt(NMK[0]), M = Integer.parseInt(NMK[1]), K = Integer.parseInt(NMK[2]);
        
        nums = new long[N];
        tree = new long[4*N];
        
        for (int i = 0; i < N; ++i) {
            nums[i] = Long.parseLong(br.readLine());
        }
        
        I(1, N, 1);

        for (int i = 0; i < M+K; ++i) {
            String[] abc = br.readLine().split(" ");
            int a = Integer.parseInt(abc[0]), b = Integer.parseInt(abc[1]);
            long c = Long.parseLong(abc[2]);

            if (a == 1) {
                long v = c - nums[b-1];
                nums[b-1] = c;
                U(1, N, 1, b, v);
            }
            else {
                System.out.println(S(1, N, b, (int)c, 1));
            }
        }

        return;
    }
}