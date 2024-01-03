package Problem;

import java.util.Scanner;

public class Problem1 {

    public static void main(String[] args) {
        int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int t = 0; t < T; t++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();

            int[][] paperFlower = new int[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    paperFlower[i][j] = scanner.nextInt();
                }
            }

            int ans = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int val = paperFlower[i][j];
                    int temp = paperFlower[i][j];

                    for (int[] d : delta) {
                        int di = d[0];
                        int dj = d[1];

                        for (int multi = 1; multi <= val; multi++) {
                            if (0 <= i + di * multi && i + di * multi < N &&
                                    0 <= j + dj * multi && j + dj * multi < M) {
                                temp += paperFlower[i + di * multi][j + dj * multi];
                            }
                        }
                    }

                    ans = Math.max(ans, temp);
                }
            }

            System.out.println("#" + (t + 1) + " " + ans);
        }
    }
}
