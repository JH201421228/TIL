package boj_15678;

import java.io.*;
import java.util.*;

public class Main {
    static int N, D;
    static long ans = 0, cur, maxK = Long.MIN_VALUE;
    static long[] K;
    static Deque<long[]> q = new ArrayDeque<>();

    static void solve() {
        for (int idx = 0; idx < N; ++idx) {
            maxK = Long.max(maxK, K[idx]);

            if (q.isEmpty()) cur = K[idx];
            else cur = q.getFirst()[0] + K[idx];

            if (cur < 0) cur = 0;

            ans = Long.max(ans, cur);

            while (!q.isEmpty() && idx - q.getFirst()[1] >= D) q.pollFirst();

            while (!q.isEmpty() && q.getLast()[0] <= cur) q.pollLast();

            q.add(new long[] {cur, idx});
        }

        if (ans > 0) System.out.println(ans);
        else System.out.println(maxK);;

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ND = br.readLine().split(" ");
        N = Integer.parseInt(ND[0]);
        D = Integer.parseInt(ND[1]);

        K = new long[N];

        String[] temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) K[idx] = Long.parseLong(temp[idx]);

        solve();

        return;
    }
}
