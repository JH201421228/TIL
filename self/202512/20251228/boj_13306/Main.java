import java.io.*;
import java.util.*;


class Main {
    static int N, Q;
    static int[] tree, parent;
    static List<String> ans;
    static Deque<int[]> question;

    static int find(int idx) {
        int root = idx;

        while (root != tree[root]) root = tree[root];

        while (idx != root) {
            int parent = tree[idx];
            tree[idx] = root;
            idx = parent;
        }

        return root;
    }

    static void union(int idx) {
        int p = find(parent[idx]);

        tree[idx] = p;

        return;
    }

    static void solve(BufferedReader br) throws IOException {
        String[] NQ = br.readLine().split(" ");
        N = Integer.parseInt(NQ[0]);
        Q = Integer.parseInt(NQ[1]);

        parent = new int[N+1];
        tree = new int[N+1];
        ans = new ArrayList<String>();
        question = new ArrayDeque<int[]>();

        parent[1] = 1;
        for (int idx = 0; idx < N-1; ++idx) parent[idx+2] = Integer.parseInt(br.readLine());
        for (int idx = 0; idx < N+1; ++idx) tree[idx] = idx;

        for (int i = 0; i < N+Q-1; ++i) {
            String[] temp = br.readLine().split(" ");

            if (temp[0].equals("1")) {
                int a = Integer.parseInt(temp[1]);
                int b = Integer.parseInt(temp[2]);
                question.push(new int[] {a, b});
            }
            else {
                int a = Integer.parseInt(temp[1]);
                question.push(new int[] {0, a});
            }
        }

        while (!question.isEmpty()) {
            int[] cur_question = question.pop();

            if (cur_question[0] != 0) {
                if (find(cur_question[0]) == find(cur_question[1])) ans.add("YES");
                else ans.add("NO");
            }
            else union(cur_question[1]);
        }

        for (int idx = ans.size(); idx > 0; --idx) System.out.println(ans.get(idx-1));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}