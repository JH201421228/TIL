package boj_28121;


import java.io.*;
import java.util.*;


class Main {
    static int N, Q;
    static int[] parent, odd, is_ans;
    static HashSet<Integer>[] sets;
    static int ans;
    static String output;


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


    static int union(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (is_ans[pa] == 1 || is_ans[pb] == 1) {
            if (is_ans[pa] == 0) {
                ans += sets[pa].size();
                is_ans[pa] = 1;
            }
            if (is_ans[pb] == 0) {
                ans += sets[pb].size();
                is_ans[pb] = 1;
            }
        }

        if (sets[pa].size() < sets[pb].size()) {
            HashSet<Integer> temp = sets[pa];
            sets[pa] = sets[pb];
            sets[pb] = temp;
        }

        parent[pb] = pa;

        if (odd[a] == odd[b]) {
            for (int v : sets[pb]) {
                sets[pa].add(v);
                odd[v] = 1- odd[v];
            }
            sets[pb].clear();
        }
        else {
            sets[pa].addAll(sets[pb]);
            sets[pb].clear();
        }

        return ans;
    }


    static void solve(BufferedReader br) throws IOException {
        String[] NQ = br.readLine().split(" ");
        N = Integer.parseInt(NQ[0]);
        Q = Integer.parseInt(NQ[1]);

        parent = new int[N+1];
        odd = new int[N+1];
        is_ans = new int[N+1];
        sets = new HashSet[N+1];

        for (int idx = 0; idx < N+1; ++idx) {
            parent[idx] = idx;
            sets[idx] = new HashSet<Integer>();
            sets[idx].add(idx);
        }

        ans = 0;

        output = "";

        for (int i = 0; i < Q; ++i) {
            String[] ab = br.readLine().split(" ");
            int a = Integer.parseInt(ab[0]);
            int b = Integer.parseInt(ab[1]);

            int pa = find(a);
            int pb = find(b);

            if (pa == pb && odd[a] == odd[b] && is_ans[pa] == 0) {
                is_ans[pa] = 1;
                ans += sets[pa].size();
            }

            if (pa != pb) ans = union(a, b);

            output += ans + "\n";
        }

        System.out.println(output);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}