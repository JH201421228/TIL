package boj_16496;

import java.io.*;
import java.util.*;



public class Main {
    static int N;
    static String temp[];
    static Stack<String> S1, S2;

    
    static void solve() {
        for (int idx = 0; idx < N; ++idx) {
            String t = temp[idx];

            if (S1.isEmpty()) S1.add(t);
            else {
                if ((S1.peek() + t).compareTo(t + S1.peek()) >= 0) {
                    if (S2.isEmpty()) S2.add(t);
                    else {
                        if ((t + S2.peek()).compareTo(S2.peek() + t) < 0) {
                            while (!S2.isEmpty() && (t + S2.peek()).compareTo(S2.peek() + t) < 0) {
                                S1.add(S2.pop());
                            }
                        }
                        S2.add(t);
                    }
                }
                else {
                    while (!S1.isEmpty() && (S1.peek() + t).compareTo(t + S1.peek()) < 0) {
                        S2.add(S1.pop());
                    }
                    S1.add(t);
                }
            }
        }

        String ans = "";

        while (!S1.isEmpty()) S2.add(S1.pop());

        while (!S2.isEmpty()) ans += S2.pop();

        if (ans.charAt(0) == '0') System.out.println(0);
        else System.out.println(ans);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        temp = br.readLine().split(" ");

        S1 = new Stack<String>();
        S2 = new Stack<String>();

        solve();

        return;
    }
    
}