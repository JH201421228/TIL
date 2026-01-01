package boj_17469;


import java.io.*;
import java.util.*;


class Main {

    static int N, Q;
    static int[] parent, tree;
    @SuppressWarnings("unchecked")
    static HashSet<Integer>[] sets;
    static Deque<int[]> questions = new ArrayDeque<>();
    static List<Integer> ans = new ArrayList<>();

    static int find(int idx) {
        int root = idx;

        while (root != tree[root]) root = tree[root];

        while (root != idx) {
            int cur = idx;
            idx = tree[idx];
            tree[cur] = root;
        }

        return root;
    }

    static void union(int idx) {
        int p = find(parent[idx]);
        tree[idx] = p;

        if (sets[p].size() < sets[idx].size()) {
            HashSet<Integer> tmp = sets[p];
            sets[p] = sets[idx];
            sets[idx] = tmp;
        }

        sets[p].addAll(sets[idx]);
        sets[idx].clear();

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NQ = br.readLine().split(" ");
        N = Integer.parseInt(NQ[0]);
        Q = Integer.parseInt(NQ[1]);

        parent = new int[N+1];
        tree = new int[N+1];
        sets = new HashSet[N+1];

        parent[1] = 1;
        for (int idx = 0; idx < N-1; ++idx) parent[idx+2] = Integer.parseInt(br.readLine());

        for (int idx = 0; idx < N; ++idx) {
            sets[idx+1] = new HashSet<>();
            sets[idx+1].add(Integer.parseInt(br.readLine()));
        }

        for (int i = 0; i < N+Q-1; ++i) {
            String[] ab = br.readLine().split(" ");
            questions.push(new int[] {Integer.parseInt(ab[0]), Integer.parseInt(ab[1])});
        }

        for (int idx = 0; idx < N+1; ++idx) tree[idx] = idx;

        while (!questions.isEmpty()) {
            int[] cur_question = questions.pop();

            if (cur_question[0] == 1) union(cur_question[1]);
            else ans.add(sets[find(cur_question[1])].size());
        }

        for (int idx = Q; idx > 0; --idx) {
            System.out.println(ans.get(idx-1));
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
    
}