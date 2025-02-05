import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<int[]> arr;
    static int[] T;

    static void U(int idx) {
        while (idx < N+1) {
            ++T[idx];
            idx += (idx & -idx);
        }
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
        N = Integer.parseInt(br.readLine());

        T = new int[N+1];

        arr = new ArrayList<int[]>();
        for (int i = 0; i < N; ++i) {
            int temp = Integer.parseInt(br.readLine());
            arr.add(new int[] {temp, i});
        }

        Collections.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < N; ++i) {
            arr.get(i)[0] = arr.get(i)[1];
            arr.get(i)[1] = i+1;
        }

        Collections.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = 0; i < N; ++i) {
            System.out.println(i + 1 - S(arr.get(i)[1]));
            U(arr.get(i)[1]);
        }
    }
}
