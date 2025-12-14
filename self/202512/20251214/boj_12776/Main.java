package boj_12776;

import java.io.*;
import java.util.*;



public class Main {
    static int N;
    static List<int[]> A, B;
    static long ans = 0, rest = 0;


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] ab = br.readLine().split(" ");
            int a = Integer.parseInt(ab[0]);
            int b = Integer.parseInt(ab[1]);

            if (a < b) A.add(new int[] {a, b});
            else B.add(new int[] {-b, -a});
        }

        A.sort((x, y) -> {
            if (x[0] != y[0]) return Integer.compare(x[0], y[0]);
            return Integer.compare(x[1], y[1]);
        });

        B.sort((x, y) -> {
            if (x[0] != y[0]) return Integer.compare(x[0], y[0]);
            return Integer.compare(x[1], y[1]);
        });

        for (int[] p : A) {
            if (rest < p[0]) {
                ans += (p[0] - rest);
                rest = p[0];
            }

            rest += (p[1] - p[0]);
        }

        for (int[] p : B) {
            long a = -p[1], b = -p[0];

            if (rest < a) {
                ans += (a - rest);
                rest = a;
            }

            rest += (b - a);
        }

        System.out.println(ans);

        return;
    }
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        A = new ArrayList<int[]>();
        B = new ArrayList<int[]>();

        solve(br);

        return;
    }
}