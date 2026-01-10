package boj_3830;


import java.io.*;
import java.util.*;


class Main {
    static int N, M;
    static int[] arr;
    static long[] state;
    static HashSet<Integer>[] sets;

    static int find(int idx) {
        int root = idx;

        while (root != arr[root]) root = arr[root];

        while (idx != root) {
            int p = arr[idx];
            arr[idx] = root;
            idx = p;
        }

        return root;
    }

    static void union(int a, int b, int w) {
        int pa = find(a);
        int pb = find(b);

        long fix = state[a] - state[b];

        if (sets[pa].size() < sets[pb].size()) {
            HashSet<Integer> temp = new HashSet<Integer>();
            temp = sets[pa];
            sets[pa] = sets[pb];
            sets[pb] = temp;
            w *= -1;
            fix *= -1;
        }

        arr[pb] = pa;

        for (int v : sets[pb]) {
            sets[pa].add(v);
            state[v] += w+fix;
        }

        sets[pb].clear();

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        arr = new int[N+1];
        state = new long[N+1];
        sets = new HashSet[N+1];

        for (int i = 0; i < N+1; ++i) {
            arr[i] = i;
            sets[i] = new HashSet<Integer>();
            sets[i].add(i);
        }

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[1]);
            int b = Integer.parseInt(temp[2]);

            int pa = find(a);
            int pb = find(b);

            if (temp[0].equals("!")) {
                int w = Integer.parseInt(temp[3]);

                if (pa != pb) union(a, b, w);
            }
            else {
                if (pa != pb) System.out.println("UNKNOWN");
                else System.out.println(state[b] - state[a]);
            }
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] NM = br.readLine().split(" ");
            N = Integer.parseInt(NM[0]);
            M = Integer.parseInt(NM[1]);

            if (N == 0 && M == 0) break;

            solve(br);
        }
        
        return;
    }
}