import java.io.*;
import java.util.*;


public class Main {
    static int Z, M, N;
    static int[] V, C;
    static List<Integer>[] G;

    static boolean B(int n) {
        for (int x : G[n]) {
            if (V[x] == 1) continue;
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
        Z = Integer.parseInt(br.readLine());

        for (int z = 0; z < Z; ++z) {
            System.out.print("Data Set ");
            System.out.print(z+1);
            System.out.println(":");

            String[] MN = br.readLine().split(" ");
            M = Integer.parseInt(MN[0]);
            N = Integer.parseInt(MN[1]);

            G = new ArrayList[N+1];
            for (int i = 1; i < N+1; ++i) {
                G[i] = new ArrayList<Integer>();
                String[] temp = br.readLine().split(" ");
                int n = Integer.parseInt(temp[0]);

                for (int j = 0; j < n; ++j) {
                    G[i].add(Integer.parseInt(temp[j+1]));
                }
            }

            C = new int[M+1];
            int ans = 0;
            for (int n = 1; n < N+1; ++n) {
                V = new int[M+1];
                if (B(n)) {
                    ++ans;
                }
            }
            System.out.println(ans);
            System.out.println();
        }
    }
}