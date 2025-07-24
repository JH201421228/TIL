import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, O;
    static int[] V, F, U;
    static Stack<Integer> S;
    static List<Integer>[] G;
    static List<List<String>> result;

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.push(n);

        for (int x : G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            List<String> temp = new ArrayList<String>();

            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = 1;
                temp.add(String.valueOf((char)(o + 64)));

                if (o == n) {
                    Collections.sort(temp);
                    result.add(temp);
                    break;
                }
            }
        }


        return p;
    }

    static void solve(int N) throws IOException {
        O = 0;
        V = new int[27];
        F = new int[27];
        U = new int[27];
        G = new ArrayList[27]; for (int idx = 0; idx < 27; ++idx) G[idx] = new ArrayList<Integer>();
        result = new ArrayList<>();
        S = new Stack<Integer>();

        for (int i = 0; i < N; ++i) {
            int[] choices = new int[6];
            String[] temp = br.readLine().split(" ");
            for (int idx = 0; idx < 6; ++idx) {
                choices[idx] = temp[idx].charAt(0) - 'A' + 1;
            }

            for (int idx = 0; idx < 5; ++idx) {
                G[choices[idx]].add(choices[5]);
                U[choices[idx]] = 1;
            }
        }

        for (int n = 1; n < 27; ++n) {
            if (V[n] == 0 && U[n] == 1) {
                scc(n);
            }
        }

        Collections.sort(result, (a, b) -> a.get(0).compareTo(b.get(0)));

        for (List<String> temp : result) {
            for (String s : temp) {
                System.out.print(s + ' ');
            }
            System.out.println();
        }
        System.out.println();

        return;
    }

    static void init() throws IOException {
        while (true) {
            N = Integer.parseInt(br.readLine());
            if (N == 0) break;

            solve(N);
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        init();

        return;
    }
}
