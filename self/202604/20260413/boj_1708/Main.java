package boj_1708;

import java.io.*;
import java.util.*;


class Main {
    static int N;
    static List<int[]> dots;

    static void solve(BufferedReader br) throws IOException {
        N = Integer.parseInt(br.readLine());
        dots = new ArrayList<>();
        for (int i = 0; i < N; ++i) {
            String[] temp = br.readLine().split(" ");
            dots.add(new int[] {Integer.parseInt(temp[0]), Integer.parseInt(temp[1])});
        }

        dots.sort((a, b) -> {
            if (a[1] == b[1]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        })        ;

        int[] origin = dots.get(0);

        List<int[]> rest = new ArrayList<>();
        for (int i = 1; i < N; ++i) rest.add(dots.get(i));

        rest.sort((a, b) -> {
            double angleA = Math.atan2(a[1] - origin[1], a[0] - origin[0]);
            double angleB = Math.atan2(b[1] - origin[1], b[0] - origin[0]);

            if (angleA == angleB) {
                long distA = 1L * (a[1] - origin[1]) * (a[1] - origin[1]) + 1L * (a[0] - origin[0]) * (a[0] - origin[0]);
                long distB = 1L * (b[1] - origin[1]) * (b[1] - origin[1]) + 1L * (b[0] - origin[0]) * (b[0] - origin[0]);
                return Long.compare(distA, distB);
            }
            return Double.compare(angleA, angleB);
        });

        List<int[]> q = new ArrayList<>();
        q.add(origin);

        for (int[] dot : rest) {
            if (q.size() < 2) {
                q.add(dot);
            }
            else {
                while (q.size() >= 2) {
                    int[] p1 = q.get(q.size()-2);
                    int[] p2 = q.get(q.size()-1);

                    int dx1 = p2[0] - p1[0];
                    int dy1 = p2[1] - p1[1];
                    int dx2 = dot[0] - p1[0];
                    int dy2 = dot[1] - p1[1];

                    if (1L * dx1 * dy2 - 1L * dx2 * dy1 > 0) break;
                    q.remove(q.size()-1);
                }
                q.add(dot);
            }
        }

        System.out.println(q.size());

        return;
    } 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }

}