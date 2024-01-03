package Problem;

import java.util.Scanner;

public class Problem4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] paper = { 50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10 };

        int T = sc.nextInt();

        for (int t = 1; t <= T; t++) {
            int money = sc.nextInt();
            System.out.print("#" + t + "\n");

            for (int p : paper) {
                System.out.print(money / p + " ");
                money %= p;
            }

            System.out.println();
        }

        sc.close();
    }
}
