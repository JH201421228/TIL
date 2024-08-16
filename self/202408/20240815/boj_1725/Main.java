package boj_1725;

import java.io.*;
import java.util.*;

public class Main {

    public static long[] H;

    public static long area(int s, int e) {
        if (s == e) {
            return H[s];
        }

        int mid = (s+e) / 2;
        int l = mid - 1;
        int r = mid + 1;
        long h = H[mid];
        long ans = H[mid];

        while (s <= l || r <= e) {
            if (s > l) {
                h = Math.min(h, H[r++]);
            }
            else if (r > e) {
                h = Math.min(h, H[l--]);
            }
            else if (H[l] >= H[r]) {
                h = Math.min(h, H[l--]);
            }
            else if (H[l] < H[r]) {
                h = Math.min(h, H[r++]);
            }

            ans = Math.max(ans, (long) h*(r-l-1));
        }
    
        return Math.max(ans, Math.max(area(s, mid), area(mid+1, e)));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        H = new long[N];

        for (int idx = 0; idx < N; ++idx) {
            H[idx] = Integer.parseInt(br.readLine());
        }

        System.out.println(area(0, N-1));
    }
}