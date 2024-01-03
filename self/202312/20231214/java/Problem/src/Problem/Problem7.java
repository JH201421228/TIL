package Problem;

import java.util.Scanner;

public class Problem7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);
		
		int T = input.nextInt();
		
		for(int t = 0; t < T; t++) {
			String bi = input.next();
			int ans = 0;
			
			for(int idx = 0; idx < bi.length()-1; idx++) {
				if(bi.charAt(idx) != bi.charAt(idx+1)) {
					ans++;
				}
			}
			
			if(bi.charAt(0) == '1') {
				ans++;
			}
			
			System.out.println("#" + (t+1) + " " + ans);
		}

	}

}
