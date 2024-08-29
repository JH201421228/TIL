import java.io.*;
import java.util.*;

public class Main {

    static long[] arr;
    static long[] lazy;

    static void lazy_U(int s, int e, int tree_idx) {
        if (lazy[tree_idx] != 0) {
            if (s == e) {
                arr[s] += lazy[tree_idx];
            }
            else {
                lazy[tree_idx*2] += lazy[tree_idx];
                lazy[tree_idx*2+1] += lazy[tree_idx];
            }
            lazy[tree_idx] = 0;
        }
    }

    static long S(int s, int e, int tree_idx, int arr_idx) {
        lazy_U(s, e, tree_idx);

        if (s == e) {
            if (s == arr_idx) {
                return arr[arr_idx];
            }
            else {
                return 0;
            }
        }

        if (arr_idx > e || arr_idx < s) {
            return 0;
        }

        int mid = (s+e) / 2;

        return S(s, mid, tree_idx*2, arr_idx) + S(mid+1, e, tree_idx*2+1, arr_idx);
    }

    static void U(int s, int e, int tree_idx, int l, int r, long val) {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            if (s == e) {
                arr[s] += val;
                return;
            }
            else {
                lazy[tree_idx*2] += val;
                lazy[tree_idx*2+1] += val;
                return;
            }
        }

        int mid = (s+e) / 2;

        U(s, mid, tree_idx*2, l, r, val);
        U(mid+1, e, tree_idx*2+1, l, r, val);
    }

    public static void main (String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        arr = new long[N+1];
        lazy = new long[4*N+1];

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            arr[i+1] = Integer.parseInt(input[i]);
        }

        int M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");

            if (Integer.parseInt(temp[0]) == 1) {
                U(1, N, 1, Integer.parseInt(temp[1]), Integer.parseInt(temp[2]), Long.parseLong(temp[3]));
            }
            else {
                System.out.println(S(1, N, 1, Integer.parseInt(temp[1])));
            }
        }

    }
}