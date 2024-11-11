import java.io.*;
import java.util.*;

public class Main {
    static int[] b, r;
    static List<List<Integer>> G;
    static int[] V;
    static int[] C;
    static List<Integer> res = new ArrayList<Integer>();
    
    static boolean is_disjoint(int a, int b) {
        if (b == 1) {
            return false;
        }

        if (a % b != 0) {
            return is_disjoint(b, a % b);
        }
        else {
            return true;
        }
    }

    static boolean B(int n) {
        for (int x : G.get(n)) {
            if (V[x] != 0) {
                continue;
            }
            V[x] = 1;

            if (C[x] == 0 || B(C[x])) {
                C[x] = n;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] MN = br.readLine().split(" ");
            int M = Integer.parseInt(MN[0]);
            int N = Integer.parseInt(MN[1]);

            if (M == 0 && N == 0) {
                break;
            }

            b = new int[M+1];
            r = new int[N+1];

            int idx = 0;

            while (true) {
                String[] temp = br.readLine().split(" ");
                for (String c : temp) {
                    b[++idx] = Integer.parseInt(c);
                }
                if (idx == M) {
                    idx = 0;
                    break;
                }
            }

            while (true) {
                String[] temp = br.readLine().split(" ");
                for (String c : temp) {
                    r[++idx] = Integer.parseInt(c);
                }
                if (idx == N) {
                    break;
                }
            }

            G = new ArrayList<>();
            for (int i = 0; i < M+1; ++i) {
                G.add(new ArrayList<Integer>());
            }

            for (int i = 1; i < M+1; ++i) {
                int x = b[i];
                for (int j = 1; j < N+1; ++j) {
                    int y = r[j];
                    if (is_disjoint(Math.max(x, y), Math.min(x, y))) {
                        G.get(i).add(j);
                    }
                }
            }

            int ans = 0;
            C = new int[N+1];
            for (int i = 1; i < M+1; ++i) {
                V = new int[N+1];
                if (B(i)) {
                    ++ans;
                }
            }

            res.add(ans);
        }

        for (int val : res) {
            System.out.println(val);
        }
    }
}