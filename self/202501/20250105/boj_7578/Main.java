import java.io.*;
import java.util.*;

public class Main {
    
    static int N;
    static int[] T = new int[1000001];
    static int[] arr;
    static long ans = 0;

    static void count(int s, int e) {
        int[] temp = new int[e-s+1];
        int mid = (s+e) >> 1;
        int i = s, j = mid+1, k = 0, cnt = mid-s+1;

        while (i < mid+1 && j < e+1) {
            if (arr[i] > arr[j]) {
                temp[k++] = arr[j++];
                ans += cnt;
            }
            else {
                temp[k++] = arr[i++];
                cnt -= 1;
            }
        }

        while (i < mid+1) temp[k++] = arr[i++];
        while (j < e+1) temp[k++] = arr[j++];

        for (int idx = 0; idx < k; ++idx) {
            arr[s+idx] = temp[idx];
        }
    }

    static void merge(int s, int e) {
        if (s < e) {
            int mid = (s+e) >> 1;
            merge(s, mid);
            merge(mid+1, e);
            count(s, e);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new int[N];

        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {
            T[Integer.parseInt(temp[i])] = i;
        }

        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < N; ++i) {
            arr[i] = T[Integer.parseInt(tmp[i])];
        }

        merge(0, N-1);

        System.out.println(ans);
    }
}