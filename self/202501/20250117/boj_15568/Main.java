import java.io.*;
import java.util.*;

public class Main {
    static int N, M, O = 0, cnt = 0;
    static int[][] interest, prefer;
    static List<Integer>[] G;
    static List<int[]>[] leafs;
    static int[] V, F;
    static Stack<Integer> S = new Stack<Integer>();

    static int scc(int n) {
        int p = ++O;
        V[n] = O;
        S.add(n);
        
        for (int x : G[n]) {
            if (V[x] == 0) {
                p = Math.min(scc(x), p);
            }
            else if (F[x] == 0) {
                p = Math.min(V[x], p);
            }
        }

        if (p == V[n]) {
            ++cnt;
            while (!S.isEmpty()) {
                int o = S.pop();
                F[o] = cnt;
                if (o == n) {
                    break;
                }
            }
        }

        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" "); N = Integer.parseInt(NM[0]); M = Integer.parseInt(NM[1]);

        interest = new int[N+1][5];
        for (int i = 1; i < N+1; ++i) {
            String[] input1 = br.readLine().split(" ");
            for (int j = 1; j < 5; ++j) {
                interest[i][j] = Integer.parseInt(input1[j-1]);
            }
        }

        G = new ArrayList[2*N+1];
        for (int i = 0; i < 2*N+1; ++i) {
            G[i] = new ArrayList<Integer>();
        }

        leafs = new ArrayList[500001];
        for (int i = 0; i < 500001; ++i) {
            leafs[i] = new ArrayList<int[]>();
        }

        prefer = new int[N+1][2];
        for (int i = 1; i < N+1; ++i) {
            String[] input2 = br.readLine().split(" ");
            for (int j = 0; j < 2; ++j) {
                prefer[i][j] = Integer.parseInt(input2[j]);
                leafs[Integer.parseInt(input2[j])].add(new int[]{i, j});
            }
        }

        for (List<int[]> leaf : leafs) {
            int n = leaf.size();

            for (int i = 0; i < n; ++i) {
                for (int j = i+1; j < n; ++j) {
                    int an = leaf.get(i)[0] + leaf.get(i)[1]*N;
                    int bn = leaf.get(j)[0] + leaf.get(j)[1]*N;

                    if (an <= N && bn <= N) {
                        G[an].add(bn+N);
                        G[bn].add(an+N);
                    }
                    else if (an <= N && bn > N) {
                        G[an].add(bn-N);
                        G[bn].add(an+N);
                    }
                    else if (an > N && bn <= N) {
                        G[an].add(bn+N);
                        G[bn].add(an-N);
                    }
                    else {
                        G[an].add(bn-N);
                        G[bn].add(an-N);
                    }
                }
            }
        }
        
        for (int i = 0; i < M; ++i) {
            String[] input3 = br.readLine().split(" ");
            
            int a = Integer.parseInt(input3[0]);
            int b = Integer.parseInt(input3[1]);
            int c = Integer.parseInt(input3[2]);
            
            for (int[] a_leaf : leafs[a]) {
                for (int[] b_leaf : leafs[b]) {
                    if (interest[a_leaf[0]][c] != interest[b_leaf[0]][c]) {
                        int an = a_leaf[0] + a_leaf[1]*N;
                        int bn = b_leaf[0] + b_leaf[1]*N;
                        
                        if (an <= N && bn <= N) {
                            G[an].add(bn+N);
                            G[bn].add(an+N);
                        }
                        else if (an <= N && bn > N) {
                            G[an].add(bn-N);
                            G[bn].add(an+N);
                        }
                        else if (an > N && bn <= N) {
                            G[an].add(bn+N);
                            G[bn].add(an-N);
                        }
                        else {
                            G[an].add(bn-N);
                            G[bn].add(an-N);
                        }
                    }
                }
            }
        }

        V = new int[2*N+1];
        F = new int[2*N+1];

        for (int i = 1; i < 2*N+1;  ++i) {
            if (V[i] == 0) {
                scc(i);
            }
        }

        List<int[]> ans_list = new ArrayList<int[]>();

        for (int i = 1; i < N+1; ++i) {
            if (F[i] == F[i+N]) {
                System.out.println("NO");
                System.exit(0);
            }
            else if (F[i] > F[i+N]) {
                ans_list.add(new int[]{prefer[i][1], i});
            }
            else {
                ans_list.add(new int[]{prefer[i][0], i});
            }
        }

        ans_list.sort(Comparator.comparing(a -> a[0]));

        System.out.println("YES");

        for (int[] ans : ans_list) {
            System.out.print(ans[1]);
            System.out.print(" ");
        }
    }    
}
