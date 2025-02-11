import java.io.*;
import java.util.*;

public class Main {
    static int C, N;
    static int[] T;
    static List<int[]> islands;
    static List<Integer> xs, ys;
    static Map<Integer, Integer> xd, yd;

    static void U(int idx) {
        while (idx < N+1) {
            ++T[idx];
            idx += (idx & -idx);
        }

        return;
    }

    static int S(int idx) {
        int res = 0;

        while (idx > 0) {
            res += T[idx];
            idx -= (idx & -idx);
        }

        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        C = Integer.parseInt(br.readLine());

        for (int z = 0; z < C; ++z) {
            N = Integer.parseInt(br.readLine());

            islands = new ArrayList<>();
            xs = new ArrayList<>();
            ys = new ArrayList<>();
            xd = new HashMap<>();
            yd = new HashMap<>();

            for (int i = 0; i < N; ++i) {
                String[] temp = br.readLine().split(" ");
                int x = Integer.parseInt(temp[0]), y = Integer.parseInt(temp[1]);

                islands.add(new int[]{x, -y});
                xs.add(x);
                ys.add(-y);
            }

            Collections.sort(xs);
            Collections.sort(ys);

            int prex = 1, prey = 1;
            for (int i = 0; i < N; ++i) {
                xd.putIfAbsent(xs.get(i), prex++);
                yd.putIfAbsent(ys.get(i), prey++);
            }

            for (int i = 0; i < N; ++i) {
                int[] island = islands.get(i);
                island[0] = xd.get(island[0]);
                island[1] = yd.get(island[1]);
            }

            islands.sort((a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));

            T = new int[N+1];
            long ans = 0;

            for (int[] island : islands) {
                int y = island[1];
                ans += S(y);
                U(y);
            }

            System.out.println(ans);
        }
    }
}
