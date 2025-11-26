package boj_1688;

import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static long[][] dots;


    static long ccw(long[] p1, long[] p2, long[] p3) {
        return (p3[0] - p1[0]) * (p2[1] - p3[1]) - (p3[1] - p1[1]) * (p2[0] - p3[0]);
    }


    static int is_cross_line(long[] p) {
        int res = 0;

        for (int idx = 0; idx < N; ++idx) {
            long[] p1 = dots[idx];
            long[] p2 = dots[(idx+1) % N];

            if (p1[1] < p2[1]) {
                long[] temp = p1;
                p1 = p2;
                p2 = temp;
            }

            if (ccw(p1, p2, p) == 0) {
                if (p[0] >= Math.min(p1[0], p2[0]) &&
                    p[0] <= Math.max(p1[0], p2[0]) &&
                    p[1] >= Math.min(p1[1], p2[1]) &&
                    p[1] <= Math.max(p1[1], p2[1])) {
                        return 1;
                }
            }

            if (p[0] > Math.max(p1[0], p2[0])) continue;

            if (p[1] >= Math.max(p1[1], p2[1])) continue;

            if (p[1] < Math.min(p1[1], p2[1])) continue;

            if (ccw(p1, p2, p) > 0) ++res;

        }

        return res % 2;
    }


    static void solve(BufferedReader br) throws IOException {
        for (int idx = 0; idx < 3; ++idx) {
            String[] temp = br.readLine().split(" ");
            long[] p = {Long.parseLong(temp[0]), Long.parseLong(temp[1])};

            if (is_cross_line(p) == 1) {
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        dots = new long[N][2];

        for (int idx = 0; idx < N; ++idx) {
            String[] temp = br.readLine().split(" ");
            dots[idx][0] = Long.parseLong(temp[0]);
            dots[idx][1] = Long.parseLong(temp[1]);
        }

        solve(br);

        return;
    }
}