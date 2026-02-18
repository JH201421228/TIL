package boj_1305;


import java.io.*;
import java.util.*;


public class Main {
    static int L;
    static String S;
    static int[] preporcess;
    static int stack_n = 0;
    
    static void solve() {
        for (int idx = 1; idx < L; ++idx) {
            while (stack_n > 0 && S.charAt(idx) != S.charAt(stack_n)) {
                stack_n = preporcess[stack_n-1];
            }

            if (S.charAt(idx) == S.charAt(stack_n)) {
                ++stack_n;
                preporcess[idx] = stack_n;
            }
        }

        System.out.println(L-preporcess[L-1]);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        L = Integer.parseInt(br.readLine());
        S = br.readLine();
        preporcess = new int[L];

        solve();

        return;
    }
}