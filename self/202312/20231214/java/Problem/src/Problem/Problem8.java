package Problem;

import java.util.Scanner;

public class Problem8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);
		
		for(int t = 1; t <= 10; t++) {
			int T = input.nextInt();
			
			int ans = 0;
			int sum1 = 0;
			int sum2 = 0;
			int sum3 = 0;
			int sum4 = 0;
			
			int[][] arr = new int[100][100];
			
			for(int i = 0; i < 100; i++) {
				for(int j = 0; j < 100; j++) {
					arr[i][j] = input.nextInt();
				}
			}
			
			for(int i = 0; i < 100; i++) {
				for(int j = 0; j < 100; j++) {
					sum1 += arr[i][j];
					sum2 += arr[j][i];
				}
				ans = Math.max(ans, sum1);
				ans = Math.max(ans, sum2);
				
				sum1 = 0;
				sum2 = 0;
				sum3 += arr[i][i];
				sum4 += arr[i][99-i];
			}
			ans = Math.max(ans, sum3);
			ans = Math.max(ans, sum4);
			
			System.out.println("#" + T + " " + ans);
		}
	}

}
