package boj_1725;

import java.io.*;
import java.util.*;

public class Semi {

    static long H[];
    static Stack<Integer> S;

    static long area(int N) {
        long ans = 0;

        for (int idx = 1; idx <= N+1; ++idx) {
            while (!S.empty() && H[S.peek()] > H[idx]) {
                int i = S.pop();
                ans = Math.max(ans, (long) H[i]*(idx-S.peek()-1));
            }
            S.add(idx);
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        H = new long[N+2];
        S = new Stack<Integer>();
        S.push(0);

        for (int idx = 1; idx <= N; ++idx) {
            H[idx] = Integer.parseInt(br.readLine());
        }

        System.out.println(area(N));
    }
}
