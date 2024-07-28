package boj_14442;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static class State {
        int i, j, k;
        State(int i, int j, int k) {
            this.i = i;
            this.j = j;
            this.k = k;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NMK = br.readLine().split(" ");
        int N = Integer.parseInt(NMK[0]), M = Integer.parseInt(NMK[1]), K = Integer.parseInt(NMK[2]);

        if (N == 1 && M == 1) {
            System.out.println(1);
            return;
        }

        int[][] G = new int[N][M];
        for (int i = 0; i < N; ++i) {
            String input = br.readLine();

            for (int j = 0; j < M; ++j) {
                G[i][j] = input.charAt(j) - '0';
            }
        }

        int[][][] V = new int[N][M][K+1];
        V[0][0][0] = 1;

        int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        Queue<State> q = new LinkedList<>();
        q.add(new State(0, 0, 0));

        while (!q.isEmpty()) {
            State s = q.poll();

            for (int[] d: delta) {
                int ii = s.i + d[0], jj = s.j + d[1];
                if (ii >= 0 && ii < N && jj >= 0 && jj < M) {
                    if (G[ii][jj] == 0 && V[ii][jj][s.k] == 0) {
                        V[ii][jj][s.k] = V[s.i][s.j][s.k] + 1;
                        q.add(new State(ii, jj, s.k));
                        if (ii == N-1 && jj == M-1) {
                            System.out.println(V[ii][jj][s.k]);
                            return;
                        }
                    }
                    else if (G[ii][jj] == 1 && s.k < K && V[ii][jj][s.k+1] == 0) {
                        V[ii][jj][s.k+1] = V[s.i][s.j][s.k] + 1;
                        q.add(new State(ii, jj, s.k+1));
                        if (ii == N-1 && jj == M-1) {
                            System.out.println(V[ii][jj][s.k+1]);
                            return;
                        }
                    }
                }
            }
        }

        System.out.println(-1);

        return;
    }    
}