package boj_2887;

import java.util.*;
import java.io.*;


public class Main {
    static ArrayList<long[]> X = new ArrayList<>();
    static ArrayList<long[]> Y = new ArrayList<>();
    static ArrayList<long[]> Z = new ArrayList<>();
    static ArrayList<long[]> M = new ArrayList<>();
    static int[] P;

    static int find(int x) {
        if (P[x] == x) {
            return x;
        }

        P[x] = find(P[x]);

        return P[x];
    }

    static void union(int x, int y) {
        int a = find(x);
        int b = find(y);

        if (a > b) {
            P[a] = b;
        }
        else {
            P[b] = a;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        P = new int[N];
        for (int i = 0; i < N; ++i) {
            P[i] = i;
        }

        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            long x = Integer.parseInt(temp[0]);
            long y = Integer.parseInt(temp[1]);
            long z = Integer.parseInt(temp[2]);

            X.add(new long[]{x, i});
            Y.add(new long[]{y, i});
            Z.add(new long[]{z, i});
        }

        X.sort(new Comparator<long[]>() {
            public int compare(long[] x1, long[] x2) {
                return Long.compare(x1[0], x2[0]);
            }
        });
        Y.sort(new Comparator<long[]>() {
            public int compare(long[] x1, long[] x2) {
                return Long.compare(x1[0], x2[0]);
            }
        });
        Z.sort(new Comparator<long[]>() {
            public int compare(long[] x1, long[] x2) {
                return Long.compare(x1[0], x2[0]);
            }
        });

        for (int i = 0; i < N-1; ++i) {
            M.add(new long[]{X.get(i+1)[0] - X.get(i)[0], X.get(i+1)[1], X.get(i)[1]});
            M.add(new long[]{Y.get(i+1)[0] - Y.get(i)[0], Y.get(i+1)[1], Y.get(i)[1]});
            M.add(new long[]{Z.get(i+1)[0] - Z.get(i)[0], Z.get(i+1)[1], Z.get(i)[1]});
        }

        M.sort(new Comparator<long[]>() {
            public int compare(long[] x1, long[] x2) {
                return Long.compare(x1[0], x2[0]);
            }
        });

        long ans = 0;
        int cnt = 0;
        int idx = 0;

        while (cnt < N-1) {
            long c = M.get(idx)[0];
            int a = (int) M.get(idx)[1];
            int b = (int) M.get(idx)[2];
            ++idx;

            if (find(a) != find(b)) {
                ans += c;
                ++cnt;

                union(a, b);
            }
        }
        
        System.out.println(ans);
    }
}