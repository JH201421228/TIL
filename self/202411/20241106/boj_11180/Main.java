import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static List<List<Integer>> G;
    static int[] C;
    static int[] V;

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

        String[] NM = br.readLine().split(" ");
        N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        G = new ArrayList<>(N+1);
        for (int i = 0; i < N+1; ++i) {
            G.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < M; ++i) {
            String[] temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]), b = Integer.parseInt(temp[1]);
            G.get(a).add(b);
            G.get(b).add(a);
        }

        C = new int[N+1];
        for (int i = 1; i < N+1; ++i) {
            V = new int[N+1];
            if (!B(i)) {
                System.out.println("Impossible");
                System.exit(0);
            }
        }

        for (int i = 1; i < N+1; ++i) {
            System.out.println(C[i]);
        }
    }
}