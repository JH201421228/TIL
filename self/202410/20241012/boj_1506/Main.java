import java.io.*;
import java.util.*;


public class Main {
    static int[] C;
    static int[] V;
    static int[] F;
    static List<List<Integer>> G;
    static ArrayList<Integer> S = new ArrayList<>();
    static ArrayList<ArrayList<Integer>> GR = new ArrayList<>();
    static int O = 0;
    static int MAX = 1000000;

    static int find_scc(int n) {
        int p = V[n] = O = O+1;
        S.add(n);

        for (int x : G.get(n)) {
            if (V[x] == 0) {
                p = Math.min(p, find_scc(x));
            }
            else if (F[x] == 0) {
                p = Math.min(p, V[x]);
            }
        }

        if (p == V[n]) {
            ArrayList<Integer> temp = new ArrayList<>();

            while (!S.isEmpty()) {
                int out = S.remove(S.size()-1);
                F[out] = 1;
                temp.add(out);

                if (out == n) {
                    GR.add(temp);
                    break;
                }
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        C = new int[N];
        V = new int[N];
        F = new int[N];

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            C[i] = Integer.parseInt(input[i]);
        }

        G = new ArrayList<>(N);
        for (int i = 0; i < N; ++i) {
            G.add(new ArrayList<>());
        }

        for (int i = 0; i < N; ++i) {
            String[] readline = br.readLine().split("");
            
            for (int j = 0; j < N; ++j) {
                if (readline[j].equals("1")) {
                    G.get(i).add(j);
                }
            }
        }

        for (int i = 0; i < N; ++i) {
            if (V[i] == 0) {
                find_scc(i);
            }
        }

        int ans = 0;
        for (ArrayList<Integer> gr : GR) {
            int v = MAX;

            for (int i : gr) {
                v = Math.min(v, C[i]);
            }

            ans += v;
        }

        System.out.println(ans);
    }    
}