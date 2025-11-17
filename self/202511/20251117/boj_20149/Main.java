// package boj_20149;


import java.io.*;
import java.util.*;


public class Main {
    static double[][] lines;
    static List<double[]> ans;

    static boolean in_ans(double[] p) {
        for (double[] q : ans) {
            if (q[0] == p[0] && q[1] == p[1]) return true;
        }

        return false;
    }

    static boolean same_dot(double[] d1, double[] d2) {
        if (d1[0] == d2[0] && d1[1] == d2[1]) return true;

        return false;
    }

    static void is_same_dot() {
        double[] d1 = {lines[0][0], lines[0][1]};
        double[] d2 = {lines[0][2], lines[0][3]};
        double[] d3 = {lines[1][0], lines[1][1]};
        double[] d4 = {lines[1][2], lines[1][3]};
        
        if (same_dot(d1, d3) && !in_ans(d1)) ans.add(d1);
        if (same_dot(d1, d4) && !in_ans(d1)) ans.add(d1);
        if (same_dot(d2, d3) && !in_ans(d2)) ans.add(d2);
        if (same_dot(d2, d4) && !in_ans(d2)) ans.add(d2);
        
        return;
    }
    
    static boolean online(double[] d1, double[] d2, double[] d3) {
        if (d3[0] >= Math.min(d1[0], d2[0]) &&
        d3[0] <= Math.max(d1[0], d2[0]) &&
        d3[1] >= Math.min(d1[1], d2[1]) &&
        d3[1] <= Math.max(d1[1], d2[1])) {
            
            if ((d1[1] - d3[1]) * (d2[0] - d3[0]) ==
            (d1[0] - d3[0]) * (d2[1] - d3[1])) {
                return true;
            }
        }
        
        return false;
    }
    
    static void is_online() {
        double[] d1 = {lines[0][0], lines[0][1]};
        double[] d2 = {lines[0][2], lines[0][3]};
        double[] d3 = {lines[1][0], lines[1][1]};
        double[] d4 = {lines[1][2], lines[1][3]};
        
        if (online(d1, d2, d3) && !in_ans(d3)) ans.add(d3);
        if (online(d1, d2, d4) && !in_ans(d4)) ans.add(d4);
        if (online(d3, d4, d1) && !in_ans(d1)) ans.add(d1);
        if (online(d3, d4, d2) && !in_ans(d2)) ans.add(d2);

        return;
    }

    static void ccw() {
        double[] d1 = {lines[0][0], lines[0][1]};
        double[] d2 = {lines[0][2], lines[0][3]};
        double[] d3 = {lines[1][0], lines[1][1]};
        double[] d4 = {lines[1][2], lines[1][3]};

        double expr1 = ((d3[0] - d2[0]) * (d2[1] - d1[1]) - 
                        (d2[0] - d1[0]) * (d3[1] - d2[1]));
        double expr2 = ((d4[0] - d2[0]) * (d2[1] - d1[1]) - 
                        (d2[0] - d1[0]) * (d4[1] - d2[1]));
        double expr3 = ((d1[0] - d3[0]) * (d3[1] - d4[1]) - 
                        (d3[0] - d4[0]) * (d1[1] - d3[1]));
        double expr4 = ((d2[0] - d3[0]) * (d3[1] - d4[1]) - 
                        (d3[0] - d4[0]) * (d2[1] - d3[1]));

        if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
            System.out.println(1);

            double x, y;

            if (d1[0] == d2[0]) {
                x = d1[0];
                y = ((d4[1] - d3[1]) * (x - d3[0])
                    / (d4[0] - d3[0]) + d3[1]);
                }
            else if (d3[0] == d4[00]) {
                x = d3[0];
                y = ((d2[1] - d1[1]) * (x - d1[0])
                    / (d2[0] - d1[0]) + d1[1]);
            }
            else {
                double alpha1 = (d2[1] - d1[1]) / (d2[0] - d1[0]);
                double alpha2 = (d4[1] - d3[1]) / (d4[0] - d3[0]);
                
                x = (alpha1 * d1[0] - alpha2 * d3[0] - d1[1] + d3[1])
                    / (alpha1 - alpha2);
                y = alpha1 * (x - d1[0]) + d1[1];
            }

            System.out.println(x + " " + y);

            return;
        }

        System.out.println(0);

        return;
    }

    static void cross_check() {
        is_same_dot();
        is_online();

        if (ans.size() > 1) {
            System.out.println(1);
            return;
        }
        else if (ans.size() == 1) {
            System.out.println(1);
            System.out.println(ans.get(0)[0] + " " + ans.get(0)[1]);
            return;
        }

        ccw();

        return;
    }

    static void solve() {
        cross_check();

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        lines = new double[2][4];
        ans = new ArrayList<double[]>();

        for (int i = 0; i < 2; ++i) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < 4; ++j) {
                lines[i][j] = Double.parseDouble(temp[j]);
            }
        }

        solve();

        return;
    }
}