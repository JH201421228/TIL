package boj_5009;

import java.io.*;
import java.util.*;

public class Main {
    static int[] cur = new int[201];
    static int[][] M = new int[201][201];
    static int[] V;
    static int[] F;
    static List<List<Integer>> G;
    static List<Integer> S;
    static int s = 0;
    static int e = 0;
    static int mid = 0;
    static int O = 0;
    static int cnt = 0;

    static void connect(int t, int N) {
        for (int i = 1; i < N+1; ++i) {
            for (int j = t+1; j < N; ++j) {
                int a = i;
                int b = M[i][j];

                if (cur[a] == cur[b]) {
                    G.get(a).add(2*N+1-b);
                    G.get(b).add(2*N+1-a);
                    G.get(2*N+1-a).add(b);
                    G.get(2*N+1-b).add(a);
                }
                else if ((cur[a]+1) % 3 == (cur[b]+2) % 3) {
                    G.get(a).add(b);
                    G.get(2*N+1-b).add(2*N+1-a);
                }
                else {
                    G.get(b).add(a);
                    G.get(2*N+1-a).add(2*N+1-b);
                }
            }
        }
    }

    static int scc(int n) {
        int p = V[n] = ++O;
        S.add(n);

        for (int x : G.get(n)) {
            if (V[x] == 0) {
                p = Math.min(p, scc(x));
            }
            else if (F[x] == 0) {
                p = Math.min(p, V[x]);
            }
        }

        if (p == V[n]) {
            ++cnt;

            while (!S.isEmpty()) {
                int out = S.get(S.size()-1);
                S.remove(S.size()-1);
                F[out] = cnt;

                if (n == out) {
                    break;
                }
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            cur[i+1] = Integer.parseInt(temp[0]);
            
            for (int j = 1; j < N; ++j) {
                M[i+1][j] = Integer.parseInt(temp[j]);
            }
        }

        e = N;
        while (s <= e) {
            Boolean checker = true;

            G = new ArrayList<>(2*N+1);
            for (int i = 0; i < 2*N+1; ++i) {
                G.add(new ArrayList<Integer>());
            }
            S = new ArrayList<>();
            V = new int[2*N+1];
            F = new int[2*N+1];
            mid = (s + e) >> 1;
            O = 0;
            cnt = 0;

            connect(mid, N);

            for (int i = 1; i < N+1; ++i) {
                if (V[i] == 0) {
                    scc(i);
                }
                if (V[2*N+1-i] == 0) {
                    scc(2*N+1-i);
                }
            }

            for (int i = 1; i < N+1; ++i) {
                if (F[i] == F[2*N+1-i]) {
                    s = mid+1;
                    checker = false;
                    break;
                }
            }
            if (checker) {
                e = mid - 1;
            }
        }

        System.out.println(s);
    }
}