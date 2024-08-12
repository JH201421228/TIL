package boj_1517;

import java.io.*;
import java.util.*;


public class Main {
    static long[] arr;
    static long[] temp;
    static long ans;

    static void merge (int s, int e) {
        int mid = (s+e) / 2;
        int i = s;
        int j = mid+1;
        int k = s;
        int cnt = 0;

        while (i <= mid && j <= e) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
                ans += (long) cnt;
            }
            else {
                temp[k++] = arr[j++];
                cnt++;
            }
        }

        if (i <= mid) {
            while (i <= mid) {
                temp[k++] = arr[i++];
                ans += (long) cnt;
            }
        }
        else {
            while (j <= e) {
                temp[k++] = arr[j++];
            }
        }

        for (int idx = s; idx <= e; ++idx) {
            arr[idx] = temp[idx];
        }
    }

    static void mergesort(int s, int e) {
        if (s < e) {
            int mid = (s+e) / 2;
            mergesort(s, mid);
            mergesort(mid+1, e);
            merge(s, e);
        } 
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        arr = new long[N];
        temp = new long[N];

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; ++i) {
            arr[i] = Long.parseLong(input[i]);
        }

        mergesort(0, N-1);

        System.out.println(ans);
    }
}
