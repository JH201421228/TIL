package boj_17131;
import java.io.*;
import java.util.*;


class Main {
    static long MOD = 1_000_000_007;
    static int N, M;
    static long[] tree;
    static Stack<int[]> coordinate;
    static List<Integer> xs;
    static Map<Integer, Integer> x_dict;

    static long S(int s, int e, int l, int r, int tree_idx) {
        if (s >= l && e <= r) return tree[tree_idx];

        if (l > e || r < s) return 0;

        int mid = (s+e)>>1;

        return S(s, mid, l, r, tree_idx<<1) + S(mid+1, e, l, r, tree_idx<<1|1);
    }

    static void U(int s, int e, int idx, int tree_idx) {
        if (s == e && s == idx) {
            ++tree[tree_idx];
            return;
        }

        if (s > idx || e < idx) return;

        int mid = (s+e)>>1;

        U(s, mid, idx, tree_idx<<1);
        U(mid+1, e, idx, tree_idx<<1|1);

        tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1];

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        coordinate = new Stack<>();
        xs = new ArrayList<>();
        x_dict = new HashMap<>();

        for (int i = 0; i < N; ++i) {
            String[] xy = br.readLine().split(" ");
            int x = Integer.parseInt(xy[0]); int y = Integer.parseInt(xy[1]);
            coordinate.add(new int[] {x, y});
            xs.add(x);
        }

        xs.sort((a, b) -> Integer.compare(a, b));
        coordinate.sort((a, b) -> Integer.compare(a[1], b[1]));

        int cur = 1;
        for (int x : xs) {
            if (!x_dict.containsKey(x)) {
                x_dict.put(x, cur++);
            }
        }

        M = x_dict.size();

        tree = new long[4*M+1];

        long ans = 0;

        while (!coordinate.isEmpty()) {
            int[] now = coordinate.pop();
            int cur_x = now[0]; int cur_y = now[1];

            List<Integer> candidates = new ArrayList<>();
            candidates.add(cur_x);

            while (!coordinate.isEmpty() && coordinate.peek()[1] == cur_y) {
                cur_x = coordinate.peek()[0]; cur_y = coordinate.peek()[1];
                coordinate.pop();
                candidates.add(cur_x);
            }

            for (int x : candidates) {
                ans += S(1, M, 1, x_dict.get(x)-1, 1) * S(1, M, x_dict.get(x)+1, M ,1);
                ans %= MOD;
            }

            for (int x : candidates) U(1, M, x_dict.get(x), 1);
        }

        System.out.println(ans);
        
        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}