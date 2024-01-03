package Problem;

import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        for (int t = 1; t <= T; t++) {
            String bi = sc.next();
            int ans = 0;
            
            for (int idx = 0; idx < bi.length() - 1; idx++) {
                if (bi.charAt(idx) != bi.charAt(idx + 1)) {
                    ans++;
                }
            }
            
            if (bi.charAt(0) == '1') {
                ans++;
            }
            
            System.out.println("#" + t + " " + ans);
        }
        
        sc.close();
    }
}
