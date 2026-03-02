package boj_28122;

import java.io.*;
import java.util.*;


class Main {
    static int N;
    static List<Integer> cnt, left, right;


    static int cal(int idx, int depth, int need) {
        if (depth > 60) return depth - need + cnt.get(idx);

        if (cnt.get(idx) <= need) return depth;

        if (left.get(idx) == -1) return cal(right.get(idx), depth+1, need+1);
        else if (right.get(idx) == -1) return cal(left.get(idx), depth+1, need+1);
        else return Math.max(cal(left.get(idx), depth+1, Math.max(1, need+1-cnt.get(right.get(idx)))), cal(right.get(idx), depth+1, Math.max(1, need+1-cnt.get(left.get(idx)))));
    }


    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");

        cnt = new ArrayList<>(); cnt.add(0);
        left = new ArrayList<>(); left.add(-1);
        right = new ArrayList<>(); right.add(-1);

        for (int i = 0; i < N; ++i) {
            long cur = Long.parseLong(temp[i]);
            int idx = 0;

            cnt.set(idx, cnt.get(idx)+1);

            for (int j = 0; j < 61; ++j) {
                if ((cur & (1L<<j)) != 0) {
                    if (right.get(idx) == -1) {
                        right.set(idx, cnt.size());
                        cnt.add(0);
                        left.add(-1);
                        right.add(-1);
                    }
                    idx = right.get(idx);
                    cnt.set(idx, cnt.get(idx)+1);
                }
                else {
                    if (left.get(idx) == -1) {
                        left.set(idx, cnt.size());
                        cnt.add(0);
                        left.add(-1);
                        right.add(-1);
                    }
                    idx = left.get(idx);
                    cnt.set(idx, cnt.get(idx)+1);
                }
            }
        }

        System.out.println(cal(0, 0, 0));

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}