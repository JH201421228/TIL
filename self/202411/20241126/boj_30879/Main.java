import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<Integer>[] G;
    static List<int[]> temp = new ArrayList<int[]>();
    static List<Integer> num = new ArrayList<Integer>();
    static int cnt = 0;
    static int s, e;
    static List<Integer> S;
    static int O;
    static int grn;
    static int[] V = new int[200001];
    static int[] F = new int[200001];

    static int scc(int n) {
        int p = V[n] = ++O;
        S.add(n);

        for (int x : G[n]) {
            if (V[x] == 0) {
                p = Math.min(p, scc(x));
            }
            else if (F[x] == 0) {
                p = Math.min(p, V[x]);
            }
        }

        if (p == V[n]) {
            ++grn;
            while (true) {
                int o = S.get(S.size()-1);
                S.remove(S.size()-1);
                F[o] = grn;

                if (o == n) {
                    break;
                }
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        num.add(0);
        temp.add(new int[] {0, 0});
        for (int i = 1; i < N+1; ++i) {
            String[] tmp = br.readLine().split(" ");
            
            if (Integer.parseInt(tmp[0]) == 1) {
                temp.add(new int[] {Integer.parseInt(tmp[1]), Integer.parseInt(tmp[2])});
                ++cnt;
            }
            else {
                num.add(cnt);
            }
        }

        s = 0;
        e = num.size()-1;
        while (s <= e) {
            int mid = (s+e) >> 1;
            Boolean is_possible = true;

            O = 0;
            grn = 0;
            S = new ArrayList<Integer>();

            G = new ArrayList[200001];
            for (int i = 0; i < 200001; ++i) {
                G[i] = new ArrayList<Integer>();
                V[i] = 0;
                F[i] = 0;
            }

            for (int i = 1; i <= num.get(mid); ++i) {
                int a = temp.get(i)[0];
                int b = temp.get(i)[1];

                if (a < 0) {
                    if (b < 0) {
                        G[-a].add(200001+b);
                        G[-b].add(200001+a);
                    }
                    else {
                        G[-a].add(b);
                        G[200001-b].add(200001+a);
                    }
                }
                else {
                    if (b < 0) {
                        G[200001-a].add(200001+b);
                        G[-b].add(a);
                    }
                    else {
                        G[200001-a].add(b);
                        G[200001-b].add(a);
                    }
                }
            }

            for (int i = 1; i < 200001; ++i) {
                if (V[i] == 0) {
                    scc(i);
                }
            }

            for (int i = 1; i < 100001; ++i) {
                if (F[i] == F[200001-i]) {
                    e = mid-1;
                    is_possible = false;
                    break;
                }
            }
            if (is_possible) {
                s = mid+1;
            }
        }

        for (int i = 0; i < e; ++i) {
            System.out.println("YES DINNER");
        }
        for (int i = 0; i < num.size()-e-1; ++i) {
            System.out.println("NO DINNER");
        }
    }
}