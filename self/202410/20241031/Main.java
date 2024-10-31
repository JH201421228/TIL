import java.io.*;
import java.util.*;

public class Main {
    static int N, M, S, V;
    static float[][] gopers;
    static float[][] holes;
    static List<List<Integer>> G;
    static int[] C;
    static int[] U;

    static boolean B(int n) {
        for (int x : G.get(n)) {
            if (U[x] != 0) {
                continue;
            }
            U[x] = 1;

            if (C[x] == 0 || B(C[x])) {
                C[x] = n;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        while ((str = br.readLine()) != null) {
            String[] NMSV = str.split(" ");

            N = Integer.parseInt(NMSV[0]); M = Integer.parseInt(NMSV[1]); S = Integer.parseInt(NMSV[2]); V = Integer.parseInt(NMSV[3]);

            C = new int[M+1];
            gopers = new float[N+1][2];
            holes = new float[M+1][2];
            G = new ArrayList<>(N+1);
            for (int i = 0; i < N+1; ++i) {
                G.add(new ArrayList<Integer>());
            }

            for (int i = 1; i < N+1; ++i) {
                String[] goper = br.readLine().split(" ");
                gopers[i][0] = Float.parseFloat(goper[0]); gopers[i][1] = Float.parseFloat(goper[1]);
            }

            for (int i = 1; i < M+1; ++i) {
                String[] hole = br.readLine().split(" ");
                holes[i][0] = Float.parseFloat(hole[0]); holes[i][1] = Float.parseFloat(hole[1]);
            }

            for (int i = 1; i < N+1; ++i) {
                float x = gopers[i][0];
                float y = gopers[i][1];
                for (int j = 1; j < M+1; ++j) {
                    float x_ = holes[j][0];
                    float y_ = holes[j][1];

                    if (Math.sqrt(Math.pow(x-x_, 2) + Math.pow(y-y_, 2)) <= S*V) {
                        G.get(i).add(j);
                    }
                }
            }

            for (int i = 1; i < N+1; ++i) {
                U = new int[M+1];
                B(i);
            }

            int ans = 0;
            for (int i = 1; i < M+1; ++i) {
                if (C[i] != 0) {
                    ++ans;
                }
            }

            System.out.println(N-ans);
        }
    }
}