import java.io.*;
import java.util.*;


public class Main {
    static int T, N, K;
    static Queue<Long> pq;

    static void solve(BufferedReader br) throws IOException {
        String[] NK = br.readLine().split(" ");
        N = Integer.parseInt(NK[0]);
        K = Integer.parseInt(NK[1]);

        pq = new PriorityQueue<Long>();

        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {
            pq.add(Long.parseLong(temp[i]));
        }

        while ((N-1) % (K-1) > 0) {
            pq.add(0l);
            ++N;
        }

        long ans = 0;
        while (pq.size() > 1) {
            long cur = 0;

            for (int i = 0; i < K; ++i) {
                cur += pq.poll();
            }

            ans += cur;
            pq.add(cur);
        }

        System.out.println(ans);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        while (T-- > 0) solve(br);

        return;
    }
}