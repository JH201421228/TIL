package Problem;

import java.util.Scanner;

public class Problem6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);
		
		int[] paper = {50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10};
		
		int T = input.nextInt();
		
		for(int t = 1; t <= T; t++) {
			int money = input.nextInt();
			System.out.println("#" + t);
			
			for(int p : paper) {
				System.out.print((money/p) + " ");
				money %= p;
			}
			System.out.println();
		}
	}

}
