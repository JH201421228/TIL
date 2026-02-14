package boj_1786;


import java.io.*;
import java.util.*;


class Main {
    static String T, P;

    static void solve(BufferedReader br) throws IOException {
        T = br.readLine();
        P = br.readLine();

        int p_len = P.length();
        int preprocess[] = new int[p_len];

        int stack_n = 0;

        for (int idx = 1; idx < p_len; ++idx) {
            while (stack_n > 0 && P.charAt(stack_n) != (P.charAt(idx))) {
                stack_n = preprocess[stack_n-1];
            }

            if (P.charAt(stack_n) == P.charAt(idx)) {
                ++stack_n;
                preprocess[idx] = stack_n;
            }
        }

        int cnt = 0;
        List<Integer> ans_list = new ArrayList<Integer>();
        int cur = 0;

        for (int idx = 0; idx < T.length(); ++idx) {
            while (cur > 0 && P.charAt(cur) != T.charAt(idx)) {
                cur = preprocess[cur-1];
            }

            if (P.charAt(cur) == T.charAt(idx)) {
                if (cur == p_len-1) {
                    ++cnt;
                    ans_list.add(idx-p_len+2);
                    cur = preprocess[cur];
                }
                else {
                    ++cur;
                }
            }
        }

        System.out.println(cnt);
        for (int ans : ans_list) {System.out.print(ans + " ");}

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}