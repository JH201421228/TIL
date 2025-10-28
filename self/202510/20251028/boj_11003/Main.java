import java.io.*;
import java.util.*;


public class Main {
    static int N, L;
    static int[] arr, D;
    static ArrayDeque<int[]> q;

    static void solve(BufferedReader br) throws IOException {
        String[] NL = br.readLine().split(" ");
        N = Integer.parseInt(NL[0]); L = Integer.parseInt(NL[1]);

        arr = new int[N];
        D = new int[N];

        q = new ArrayDeque<int[]>();

        String[] temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) arr[idx] = Integer.parseInt(temp[idx]);

        for (int idx = 0; idx < N; ++idx) {
            if (q.isEmpty()) {
                q.add(new int[] {arr[idx], idx});
            }
            else {
                if (idx - q.peekFirst()[1] >= L) {
                    q.poll();
                }

                int cur = arr[idx];

                while (!q.isEmpty() && q.peekLast()[0] > cur) {
                    q.pollLast();
                }

                q.add(new int[] {cur, idx});
            }

            D[idx] = q.peekFirst()[0];
        }

        for (int idx = 0; idx < N; ++idx) {
            System.out.print(D[idx]);
            System.out.print(' ');
        }

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(br);

        return;
    }
}