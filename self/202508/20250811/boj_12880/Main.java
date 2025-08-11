import java.io.*;
import java.util.*;

public class Main {
    static int N, cnt, interval = Integer.MAX_VALUE;
    static int[] V;
    static int[][] G;
    static List<Integer> weights;

    static void dfs(int n, int l, int r, boolean flag) {
        ++cnt;
        V[n] = 1;

        for (int x = 0; x < N; ++x) {
            if (flag) {
                if (V[x] == 0 && l <= G[n][x] && G[n][x] <= r) dfs(x, l, r, flag);
            }
            else {
                if (V[x] == 0 && l <= G[x][n] && G[x][n] <= r) dfs(x, l, r, flag);
            }
        }
        
        return;
    }

    static boolean checker(int l, int r) {
        Arrays.fill(V, 0);
        cnt = 0;
        dfs(0, l, r, false);
        if (cnt != N) return false;

        Arrays.fill(V, 0);
        cnt = 0;
        dfs(0, l, r, true);

        return cnt == N;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        V = new int[N];
        G = new int[N][N];
        weights = new ArrayList<Integer>();
        Set<Integer> weights_set = new HashSet<Integer>();
        
        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < N; ++j) {
                G[i][j] = Integer.parseInt(temp[j]);
                weights_set.add(G[i][j]);
            }
        }

        for (int w : weights_set) weights.add(w);
        weights.sort((a, b) -> a - b);

        int s = 0;
        for (int e = 0; e < weights.size(); ++e) {
            for (; s <= e; ++s) {
                if (checker(weights.get(s), weights.get(e))) {
                    interval = Math.min(interval, weights.get(e) - weights.get(s));
                }
                else break;
            }
        }

        System.out.println(interval);

        return;
    }
}
