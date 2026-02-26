package boj_13505;


import java.io.*;
import java.util.*;


class Main {
    static int N, mask = 0, cand = 0, attempt = 0;
    static int[] nums;
    static Set<Integer> S;

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());

        nums = new int[N];
        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) nums[i] = Integer.parseInt(temp[i]);

        S = new HashSet<>();

        for (int i = 29; i >= 0; --i) {
            mask |= 1<<i;
            attempt = cand | (1<<i);

            S.clear();

            for (int n : nums) {
                int tmp = n & mask;
                if (S.contains(tmp ^ attempt)) {
                    cand = attempt;
                    break;
                }
                S.add(tmp);
            }
        }

        System.out.println(cand);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}