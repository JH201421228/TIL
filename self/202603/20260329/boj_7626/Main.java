package boj_7626;


import java.io.*;
import java.util.*;



public class Main {
    static int N;
    static int[] yss = new int[200_001 * 2];
    static int[] counts = new int[200_001 * 8];
    static int[] tree = new int[200_001 * 8];

    static List<int[]> xs = new ArrayList<>();
    static Set<Integer> ys = new TreeSet<>();
    static Map<Integer, Integer> y_to_cnt = new HashMap<>();


    static void U(int s, int e, int l, int r, int tree_idx, int val) {
        if (s > r || e < l) return;

        if (s >= l && e <= r) counts[tree_idx] += val;

        else {
            int mid = (s+e)>>1;
            U(s, mid, l, r, tree_idx<<1, val);
            U(mid+1, e, l, r, tree_idx<<1|1, val);
        }

        if (counts[tree_idx] > 0) tree[tree_idx] = yss[e+1] - yss[s];
        else {
            if (s == e) tree[tree_idx] = 0; 
            else tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1];
        }

        return;
    }

    
    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            int x1, x2, y1, y2;
            x1 = Integer.parseInt(temp[0]);
            x2 = Integer.parseInt(temp[1]);
            y1 = Integer.parseInt(temp[2]);
            y2 = Integer.parseInt(temp[3]);

            xs.add(new int[] {x1, y1, y2, 1});
            xs.add(new int[] {x2, y1, y2, -1});
            ys.add(y1);
            ys.add(y2);
        }

        xs.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            if (a[2] != b[2]) return Integer.compare(a[2], b[2]);
            return Integer.compare(a[3], b[3]);
        });

        int cnt = 0;

        for (int y : ys) {
            ++cnt;
            y_to_cnt.put(y, cnt);
            yss[cnt] = y;
        }

        long ans = 0;

        int prev, yy1, yy2;
        prev = xs.get(0)[0]; yy1 = xs.get(0)[1]; yy2 = xs.get(0)[2];

        U(1, cnt-1, y_to_cnt.get(yy1), y_to_cnt.get(yy2)-1, 1, 1);

        for(int idx = 1; idx < xs.size(); ++idx) {
            int x = xs.get(idx)[0], y1 = xs.get(idx)[1], y2 = xs.get(idx)[2], flag = xs.get(idx)[3];

            ans += (long) (x - prev) * tree[1];
            prev = x;
            U(1, cnt-1, y_to_cnt.get(y1), y_to_cnt.get(y2)-1, 1, flag);
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

