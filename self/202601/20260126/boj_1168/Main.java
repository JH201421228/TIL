import java.io.*;
import java.util.*;


class Main {
    static int N, K;
    static int tree[] = new int[400_005];

    static int I(int s, int e, int tree_idx) {
        if (s == e) {
            tree[tree_idx] = 1;
            return 1;
        }

        int mid = (s+e)>>1;

        tree[tree_idx] = I(s, mid, tree_idx<<1) + I(mid+1, e, tree_idx<<1|1);

        return tree[tree_idx];
    }

    static int U(int s, int e, int tree_idx, int target) {
        tree[tree_idx] -= 1;

        if (s == e) return s;

        int mid = (s+e)>>1;

        if (target <= tree[tree_idx<<1]) return U(s, mid, tree_idx<<1, target);
        else return U(mid+1, e, tree_idx<<1|1, target-tree[tree_idx<<1]);
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]);
        K = Integer.parseInt(NK[1]);

        I(1, N, 1);

        int cur = K;
        System.out.print("<");
        for (int t = 0; t < N; ++t) {
            System.out.print(U(1, N, 1, cur));

            if (t == N-1) break;
            cur = (cur+K-2) % (N-t-1) + 1;
            System.out.print(", ");
        }
        System.out.println(">");

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}