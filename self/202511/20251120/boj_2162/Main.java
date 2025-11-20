package boj_2162;

import java.io.*;
import java.util.*;

public class Main {
    static double[][] lines;
    static int N;
    static int[] V;
    static List<Integer>[] G;
    static Queue<Integer> q;


    static boolean is_same_dot(double[] d1, double[] d2, double[] d3, double[] d4) {
        if ((d1[0] == d3[0] && d1[1] == d3[1]) ||
            (d1[0] == d4[0] && d1[1] == d4[1]) ||
            (d2[0] == d3[0] && d2[1] == d3[1]) ||
            (d2[0] == d4[0] && d2[1] == d4[1])) {
            return true;
        }

        return false;
    }


    static boolean is_online(double[] d1, double[] d2, double[] d3) {
        if (d3[0] >= Math.min(d1[0], d2[0]) &&
            d3[0] <= Math.max(d1[0], d2[0]) &&
            d3[1] >= Math.min(d1[1], d2[1]) &&
            d3[1] <= Math.max(d1[1], d2[1]) &&
            ((d1[1] - d3[1]) * (d2[0] - d3[0])) ==
            ((d1[0] - d3[0]) * (d2[1] - d3[1]))) {
            return true;
        }

        return false;
    }


    static boolean ccw(double[] d1, double[] d2, double[] d3, double[] d4) {
        double expr1 = (d3[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d3[1] - d2[1]);
        double expr2 = (d4[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d4[1] - d2[1]);
        double expr3 = (d1[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d1[1] - d4[1]);
        double expr4 = (d2[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d2[1] - d4[1]);

        if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
            return true;
        }

        return false;
    }

    
    static boolean cross_check(double[] d1, double[] d2, double[] d3, double[] d4) {
        if (is_same_dot(d1, d2, d3, d4)) return true;

        if (is_online(d1, d2, d3)) return true;

        if (is_online(d1, d2, d4)) return true;

        if (is_online(d3, d4, d1)) return true;

        if (is_online(d3, d4, d2)) return true;

        if (ccw(d1, d2, d3, d4)) return true;

        return false;
    }


    static int travle(int m) {
        int res = 0;

        V[m] = 1;
        q.add(m);

        while (!q.isEmpty()) {
            int n = q.poll();
            
            ++res;

            for (int x : G[n]) {
                if (V[x] == 0) {
                    V[x] = 1;
                    q.add(x);
                }
            }
        }

        return res;
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        lines = new double[N+1][4];
        V = new int[N+1];
        G = new ArrayList[N+1]; for (int idx = 0; idx < N+1; ++idx) G[idx] = new ArrayList<Integer>();
        q = new ArrayDeque<Integer>();

        for (int idx = 0; idx < N; ++idx) {
            String[] temp = br.readLine().split(" ");
            lines[idx][0] = Double.parseDouble(temp[0]);
            lines[idx][1] = Double.parseDouble(temp[1]);
            lines[idx][2] = Double.parseDouble(temp[2]);
            lines[idx][3] = Double.parseDouble(temp[3]);
        }

        for (int i = 0; i < N; ++i) {
            for (int j = i+1; j < N; ++j) {
                if (cross_check(new double[] {lines[i][0], lines[i][1]}, 
                                new double[] {lines[i][2], lines[i][3]}, 
                                new double[] {lines[j][0], lines[j][1]}, 
                                new double[] {lines[j][2], lines[j][3]})) {
                    G[i+1].add(j+1);
                    G[j+1].add(i+1);
                }
            }
        }

        int res = 0, cnt = 0;

        for (int n = 1; n < N+1; ++n) {
            if (V[n] == 0) {
                ++cnt;
                res = Math.max(res, travle(n));
            }
        }

        System.out.println(cnt);
        System.out.println(res);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
    
}