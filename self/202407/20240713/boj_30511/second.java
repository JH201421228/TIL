import java.io.*;
import java.lang.reflect.Array;
import java.util.*;



public class second {
    static List<Integer>[] G = new ArrayList[10001];
    static int[] C = new int[10001];
    static int[] V = new int[10001];
    static int[][] Ss = new int[101][101], Sg = new int[101][101];

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

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]), M = Integer.parseInt(input[1]);

        String[] S = new String[N];
        for (int i = 0; i < N; i++) {
            S[i] = br.readLine();
        }

        int cnt_s = 0, cnt_g = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (S[i].charAt(j) == 'S') {
                    Ss[i][j] = ++cnt_s;
                }
                else if (S[i].charAt(j) == 'G') {
                    Sg[i][j] = ++cnt_g;
                }
            }
        }

        for (int i = 0; i <= cnt_s; i++) {
            G[i] = new ArrayList<>();
        }

        int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (S[i].charAt(j) == 'S') {
                    for (int[] d : delta) {
                        int ii = i+d[0], jj = j+d[1];
                        if (ii >= 0 && ii < N && jj >= 0 && jj < M&& S[ii].charAt(jj) == 'G') {
                            if ((i+2*d[0] >= 0 && i+2*d[0] < N && j+2*d[1] >= 0 && j+2*d[1] < M && S[i+2*d[0]].charAt(j+2*d[1]) == 'M') || (i-d[0] >= 0 && i-d[0] < N && j-d[1] >= 0 && j-d[1] < M && S[i-d[0]].charAt(j-d[1]) == 'M')) {
                                G[Ss[i][j]].add(Sg[ii][jj]);
                            }
                        }
                    }
                }
            }
        }

        int ans = 0;
        for (int i = 0; i <= cnt_s; i++) {
            Arrays.fill(V, 0, cnt_g+1, 0);
            if (B(i)) {
                ++ans;
            }
        }

        System.out.println(ans);
    }
}
