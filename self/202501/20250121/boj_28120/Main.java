import java.io.*;
import java.util.*;

public class Main {
    static int N, K, X;
    static int[] V, C;
    static List<Integer>[] G;
    static List<List<Integer>> I;

    static boolean B(int n) {
        for (int x : G[n]) {
            if (V[x] != 0) continue;
            V[x] = 1;

            if (C[x] == 0 || B(C[x])) {C[x] = n; return true;}
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] NKX = br.readLine().split(" ");
        N = Integer.parseInt(NKX[0]); K = Integer.parseInt(NKX[1]); X = Integer.parseInt(NKX[2]);

        G = new ArrayList[N+1]; for (int i = 0; i < N+1; ++i) {G[i] = new ArrayList<Integer>();}
        I = new ArrayList<List<Integer>>(); for (int i = 0; i < N; ++i) {I.add(new ArrayList<Integer>());}
        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            I.get(i).add(0); I.get(i).add(i+1);
            
            for (int j = 1; j < Integer.parseInt(temp[0])+1; ++j) {
                I.get(i).add(Integer.parseInt(temp[j]));
            }
        }

        String[] score = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {I.get(i).set(0, Integer.parseInt(score[i]));}
        I.sort(Comparator.comparing((List<Integer> a) -> a.get(0)).reversed());
        
        for (int i = 0; i < N; ++i) {
            int n = I.get(i).size();
            for (int j = 2; j < n; ++j) {
                int v = I.get(i).get(j);
                for (int k = 0; k < X; ++k) {
                    G[i+1].add((v-1)*X+1+k);
                    // System.out.println((v-1)*X+1+k);
                }
            }
        }

        C = new int[16];
        for (int i = 1; i < N+1; ++i) {
            V = new int[16];
            B(i);
        }

        List<List<Integer>> ans_list = new ArrayList<List<Integer>>();
        for (int i = 0; i < K; ++i) ans_list.add(new ArrayList<Integer>());
        for (int i = 1; i < 16; ++i) {
            if (C[i] != 0) {
                ans_list.get((i-1)/X).add(I.get(C[i]-1).get(1));
            }
        }

        // for (int x : C) {
        //     System.out.print(x + " ");
        // }

        for (List<Integer> ans : ans_list) {
            System.out.print(ans.size() + " ");
            for (int x : ans) {
                System.out.print(x + " ");
            }
            System.out.println();
        }
    }
}
