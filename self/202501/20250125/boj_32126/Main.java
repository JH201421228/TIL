import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[][] M;
    static List<Integer>[] G;
    static int[] C, V;

    static boolean B(int n) {
        for (int x : G[n]) {
            if (V[x] == 1) {
                continue;
            }
            V[x] = 1;

            if (C[x] == 0 || B(C[x])) {
                C[x] = n;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NK = br.readLine().split(" "); N = Integer.parseInt(NK[0]); K = Integer.parseInt(NK[1]);

        M = new int[N][K];
        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < K; ++j) {
                M[i][j] = Integer.parseInt(temp[j]);
            }
        }

        G = new ArrayList[K+1]; for (int i = 0; i < K+1; ++i) G[i] = new ArrayList<Integer>();
        for (int t = 0; t < K; ++t) {
            for (int d = 0; d < N; ++d) {
                if (M[d][K-1-t] == 1) {
                    G[t+1].add(d+1);
                }
            }
        }

        int ans = 0, camera = 0;

        C = new int[N+1];
        for (int i = 1; i < K+1; ++i) {
            V = new int[N+1];
            if (B(i)) {
                if (K+1-i < ans-camera+2) {
                    System.out.println(ans);
                    System.exit(0);
                }
                ++ans;
            }
            else {
                if (camera < ans) {
                    ++camera;
                }
            }
        }

        System.out.println(ans);
    }
}