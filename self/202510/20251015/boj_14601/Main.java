package boj_14601;

import java.io.*;
import java.util.*;


public class Main {
    static int K, ti, tj, cnt = 1;
    static int[][] ans;
    static final int[][] delta = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};

    static int[][] set_num(int i, int j, int ti, int tj, int l) {
        int[][] res = new int[4][2];
        
        for (int a = 0; a < 4; ++a) Arrays.fill(res[a], -1);

        if (ti >= i && ti < i+l && tj >= j && tj < j+l) {
            ;
        }
        else {
            ans[i+l-1][j+l-1] = cnt;
            res[0][0] = i+l-1;
            res[0][1] = j+l-1;
        }

        if (ti >= i+l && ti < i+l*2 && tj >= j && tj < j+l) {
            ;
        }
        else {
            ans[i+l][j+l-1] = cnt;
            res[1][0] = i+l;
            res[1][1] = j+l-1;
        }

        if (ti >= i && ti < i+l && tj >= j+l && tj < j+l*2) {
            ;
        }
        else {
            ans[i+l-1][j+l] = cnt;
            res[2][0] = i+l-1;
            res[2][1] = j+l;
        }

        if (ti >= i+l && ti < i+l*2 && tj >= j+l && tj < j+l*2) {
            ;
        }
        else {
            ans[i+l][j+l] = cnt;
            res[3][0] = i+l;
            res[3][1] = j+l;
        }

        ++cnt;

        return res;
    }

    static void dq(int i, int j, int ti, int tj, int l) {
        if (l == 1) {
            for (int di = 0; di < 2; ++di) {
                for (int dj = 0; dj < 2; ++dj) {
                    if (ans[i+di][j+dj] == 0) {
                        ans[i+di][j+dj] = cnt;
                    }
                }
            }
            ++cnt;
            return;
        }

        int[][] temp = set_num(i, j, ti, tj, l);

        for (int idx = 0; idx < 4; ++idx) {
            int di = delta[idx][0] * l;
            int dj = delta[idx][1] * l;

            if (temp[idx][0] != -1 && temp[idx][1] != -1) {
                dq(i+di, j+dj, temp[idx][0], temp[idx][1], l/2);
            }
            else {
                dq(i+di, j+dj, ti, tj, l/2);
            }
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        K = Integer.parseInt(br.readLine());
        String[] titj = br.readLine().split(" ");

        ti = (1<<K) - Integer.parseInt(titj[1]);
        tj = Integer.parseInt(titj[0]) - 1;

        ans = new int[1<<K][1<<K];
        ans[ti][tj] = -1;

        dq(0, 0, ti, tj, (1<<(K-1)));

        for (int i = 0; i < (1<<K); ++i) {
            for (int j = 0; j < (1<<K); ++j) {
                System.out.print(ans[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }

        return;
    }
}