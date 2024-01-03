package Problem;

import java.util.Scanner;	

public class Problem5 {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] delta = {{1, 0}, {0, 1} ,{-1, 0}, {0, -1}};
		
		Scanner input = new Scanner(System.in);
		int T = input.nextInt();
		
		for (int t = 0; t < T; t++) {
			int N = input.nextInt();
			int M = input.nextInt();
			
			int[][] ballon = new int[N][M];
			
			for (int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++) {
					ballon[i][j] = input.nextInt();
				}
			}
			
			int ans = 0;
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					int val = ballon[i][j];
					int temp = ballon[i][j];
					
					for (int[] d : delta) {
						int di = d[0];
						int dj = d[1];
						
						for (int multi = 1; multi <= val; multi++) {
							if (0 <= i+di*multi && i+di*multi < N && 0 <= j+dj*multi && j+dj*multi < M) {
								temp += ballon[i+di*multi][j+dj*multi];
							}
						}
					}
					ans = Math.max(ans, temp);
				}
			}
			System.out.println("#" + (t+1) + " " + ans);
		}

	}

}
