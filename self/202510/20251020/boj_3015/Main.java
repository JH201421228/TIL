package boj_3015;

import java.io.*;
import java.util.*;


public class Main {
    static int N, cur, cur_cnt;
    static int[] arr;
    static long ans = 0;
    static Stack<int[]> S;

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        S = new Stack<>();

        for (int i = 0; i < N; ++i) arr[i] = Integer.parseInt(br.readLine());

        for (int idx = 0; idx < N; ++idx) {
            if (!S.isEmpty()) {
                ++ans;
                cur = arr[idx];
                cur_cnt = 1;

                while (!S.isEmpty() && S.peek()[0] <= cur) {
                    int[] temp = S.pop();

                    if (!S.isEmpty()) {
                        ans += temp[1];
                    }
                    else {
                        ans += temp[1]-1;
                    }

                    if (temp[0] == cur) {
                        cur_cnt += temp[1];
                        break;
                    }
                }

                S.add(new int[] {cur, cur_cnt});
            }
            else {
                S.add(new int[] {arr[idx], 1});
            }
        }

        System.out.println(ans);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
    
}