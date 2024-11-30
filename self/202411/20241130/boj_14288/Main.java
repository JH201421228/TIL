import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static List<Integer> G[];
    static int[] A;
    static int[] E;
    static int cnt = 0;
    static int[] tree1;
    static int[] tree2;
    static int[] lazy1;
    static int[] lazy2;
    static boolean is_down_direction = true;

    static void dfs(int n) {
        A[n] = ++cnt;
        for (int x : G[n]) {
            dfs(x);
        }
        E[n] = cnt;
    }

    static void lazy_U(int s, int e, int idx, int[] tree, int[] lazy) {
        if (lazy[idx] != 0) {
            tree[idx] += (e-s+1) * lazy[idx];
            if (s != e) {
                lazy[idx*2] += lazy[idx];
                lazy[idx*2+1] += lazy[idx];
            }
            lazy[idx] = 0;
        }
    }

    static void U(int s, int e, int idx, int l, int r, int v, int[] tree, int[] lazy) {
        lazy_U(s, e, idx, tree, lazy);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            lazy[idx] += v;
            lazy_U(s, e, idx, tree, lazy);
            return;
        }

        int mid = (s+e) >> 1;
        U(s, mid, idx*2, l, r, v, tree, lazy);
        U(mid+1, e, idx*2+1, l, r, v, tree, lazy);
        tree[idx] = tree[idx*2] + tree[idx*2+1];
    }

    static int S(int s, int e, int idx, int l, int r, int[] tree, int[] lazy) {
        lazy_U(s, e, idx, tree, lazy);

        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[idx];
        }

        int mid = (s+e) >> 1;
        return S(s, mid, idx*2, l, r, tree, lazy) + S(mid+1, e, idx*2+1, l, r, tree, lazy);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        N = Integer.parseInt(NM[0]);
        M = Integer.parseInt(NM[1]);
        
        A = new int[N+1];
        E = new int[N+1];

        tree1 = new int[4*N+1];
        tree2 = new int[4*N+1];
        lazy1 = new int[4*N+1];
        lazy2 = new int[4*N+1];

        G = new ArrayList[N+1];
        for (int i = 0; i < N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }
        String[] temp = br.readLine().split(" ");
        for (int i = 1; i < N; ++i) {
            G[Integer.parseInt(temp[i])].add(i+1);
        }

        dfs(1);

        for (int i = 0; i < M; ++i) {
            String[] tmp = br.readLine().split(" ");

            if (Integer.parseInt(tmp[0]) == 1) {
                if (is_down_direction) {
                    U(1, N, 1, A[Integer.parseInt(tmp[1])], E[Integer.parseInt(tmp[1])], Integer.parseInt(tmp[2]), tree1, lazy1);
                }
                else {
                    U(1, N, 1, A[Integer.parseInt(tmp[1])], A[Integer.parseInt(tmp[1])], Integer.parseInt(tmp[2]), tree2, lazy2);
                }
            }
            else if (Integer.parseInt(tmp[0]) == 2) {
                System.out.println(S(1, N, 1, A[Integer.parseInt(tmp[1])], A[Integer.parseInt(tmp[1])], tree1, lazy1) + S(1, N, 1, A[Integer.parseInt(tmp[1])], E[Integer.parseInt(tmp[1])], tree2, lazy2));
            }
            else {
                is_down_direction = !is_down_direction;
            }
        }
    }
}