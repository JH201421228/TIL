package Problem;

import java.util.Scanner;
import java.util.Arrays;

public class Problem9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		int[] N_list = new int[N];
		for(int i = 0; i < N; i++) {
			N_list[i] = input.nextInt();
		}
		
		int M = input.nextInt();
		int[] M_list = new int[M];
		for(int i = 0; i < M; i++) {
			M_list[i] = input.nextInt();
		}
		
		Arrays.sort(N_list);
		
		for(int num : M_list) {
			if(Arrays.binarySearch(N_list, num) >= 0) {
				System.out.println(1);
			}
			else {
				System.out.println(0);
			}
		}

	}

}
