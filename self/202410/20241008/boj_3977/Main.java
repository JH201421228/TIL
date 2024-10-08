package boj_3977;

import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

class Main {
    static List<List<Integer>> G;
    static List<Integer> S;
    static int[] V;
    static int[] F;
    static int[] C;
    static int O;
    static int GN;

    static int find_scc(int n) {
        ++O;
        int P = V[n] = O;
        S.add(n);

        for (int x : G.get(n)) {
            if (V[x] == -1) {
                P = Math.min(P, find_scc(x));
            }
            else if (F[x] == 0) {
                P = Math.min(P, V[x]);
            }
        }

        if (P == V[n]) {
            ++GN;

            while (!S.isEmpty()) {
                int out = S.remove(S.size()-1);
                F[out] = GN;

                if (out == n) {
                    break;
                }
            }
        }

        return P;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            String[] temp = br.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), M = Integer.parseInt(temp[1]);

            G = new ArrayList<>(N);

            for (int j = 0; j < N; ++j) {
                G.add(new ArrayList<>());
            }

            for (int j = 0; j < M; ++j) {
                String[] AB = br.readLine().split(" ");
                int a = Integer.parseInt(AB[0]), b = Integer.parseInt(AB[1]);

                G.get(a).add(b);
            }
            br.readLine();

            S = new ArrayList<>();
            V = new int[N]; Arrays.fill(V, -1);
            F = new int[N];
            O = 0;
            GN = 0;

            for (int j = 0; j < N; ++j) {
                if (V[j] == -1) {
                    find_scc(j);
                }
            }

            C = new int[GN+1];

            for (int j = 0; j < N; ++j) {
                for (int k : G.get(j)) {
                    if (F[j] != F[k]) {
                        C[F[k]] = F[j];
                    }
                }
            }

            List<Integer> arr = new ArrayList<>();

            for (int j = 1; j < GN+1; ++j) {
                if (C[j] == 0) {
                    arr.add(j);
                }
            }

            if (arr.size() > 1) {
                System.out.println("Confused");
            }
            else {
                for (int j = 0; j < N; ++j) {
                    if (F[j] == arr.get(0)) {
                        System.out.println(j);
                    }
                }
            }

            System.out.println();
        }
    }
}