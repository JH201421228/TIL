package boj_12456;

import java.io.*;
import java.util.*;


public class Main {

    static class Node {
        long s, c, t;
        
        Node(long s, long c, long t) {
            this.s = s;
            this.c = c;
            this.t = t;
        }
    }

    static int T, N, idx, cur_s, cur_c, cur_t;
    static long K, cur_d, nxt_d, gap, ans;
    static List<Node> arr;
    static Queue<Node> pq;

    static long solve(BufferedReader br) throws IOException {
        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]); K = Long.parseLong(NK[1]);

        arr = new ArrayList<Node>();
        pq = new PriorityQueue<Node>(
            (a, b) -> Long.compare(b.s, a.s)
        );

        for (int i = 0; i < N; ++i) {
            String[] cts = br.readLine().split(" ");
            long c, t, s; c = Long.parseLong(cts[0]); t = Long.parseLong(cts[1]); s = Long.parseLong(cts[2]);
            arr.add(new Node(s, c, t));
        }

        arr.sort((a, b) -> Long.compare(b.t, a.t));

        cur_d = K;
        idx = 0;
        ans = 0;

        while (cur_d > 0) {
            while (idx < N && arr.get(idx).t >= cur_d) {
                pq.add(arr.get(idx++));
            }

            if (idx < N) nxt_d = arr.get(idx).t;
            else nxt_d = 0;

            gap = cur_d - nxt_d;

            while (gap > 0 && !pq.isEmpty()) {
                Node top = pq.poll();
                long amount = Math.min(gap, top.c);

                ans += amount * top.s;
                gap -= amount;
                top.c -= amount;

                if (top.c > 0) pq.add(top);
            }

            cur_d = nxt_d;
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            System.out.println("Case #" + (i+1) + ": " + solve(br));
        }

        return;
    }
}
