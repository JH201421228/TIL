import java.io.*;
import java.util.*;


class Main {

    static int N, M;
    static int[] parent;
    static long[] state, debt;
    static HashSet<Integer>[] sets;

    static int find(int idx) {
        int root = idx;

        while (root != parent[root]) root = parent[root];

        while (root != idx) {
            int p = parent[idx];
            parent[idx] = root;
            idx = p;
        }

        return root;
    }

    static void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (sets[pa].size() < sets[pb].size()) {
            int tmp = pa;
            pa = pb; pb = tmp;
        }

        parent[pb] = pa;

        long cost = (debt[pa] / sets[pa].size()) - (debt[pb] / sets[pb].size());

        debt[pa] = (debt[pa] / sets[pa].size()) * (sets[pa].size() + sets[pb].size());

        for (int v : sets[pb]) {
            sets[pa].add(v);
            state[v] += cost;
        }

        sets[pb].clear();

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NM = br.readLine().split(" ");
        N = Integer.parseInt(NM[0]);
        M = Integer.parseInt(NM[1]);

        parent = new int[N+1];
        state = new long[N+1];
        debt = new long[N+1];
        sets = new HashSet[N+1];

        for (int idx = 0; idx < N+1; ++idx) {
            parent[idx] = idx;
            sets[idx] = new HashSet<Integer>();
            sets[idx].add(idx);
        }

        for (int i = 0; i < M; ++i) {
            String[] abc = br.readLine().split(" ");
            int a = Integer.parseInt(abc[0]);
            int b = Integer.parseInt(abc[1]);
            long c = Long.parseLong(abc[2]);

            if (a == 1) union(b, (int) c);
            else {
                debt[find(b)] += c;
                state[b] += c;
            }
        }

        int p = find(1);

        if (debt[p] != 0) {
            long cost = debt[p] / N;

            for (int idx = 1; idx < N+1; ++idx) state[idx] -= cost;
        }

        String ans = "";
        int cnt = 0;

        for (int idx = 1; idx < N+1; ++idx) {
            if (idx == p || state[idx] == 0) continue;
            
            ++cnt;

            if (state[idx] > 0) ans += p + " " + idx + " " + state[idx] + "\n";
            else ans += idx + " " + p + " " + -state[idx] + "\n";
        }

        System.out.println(cnt);
        System.out.println(ans);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}