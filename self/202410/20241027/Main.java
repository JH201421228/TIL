import java.util.*;
import java.io.*;


public class Main {
    static char[][] M;
    static int[][] N;
    static String temp = "";
    static boolean check = false;
    static List<String> names;
    static List<int[]> cities;
    static int names_num = 0;
    static int cities_num = 0;
    static int[][] delta = {{1, 1}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}, {-1, -1}, {1, -1}, {-1, 1}};
    static List<List<Integer>> G;
    static int[] F;
    static int[] V;

    static boolean B(int n) {
        for (int x : G.get(n)) {
            if (V[x] != 0) {
                continue;
            }
            V[x] = 1;

            if (F[x] == 0 || B(F[x])) {
                F[x] = n;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] RC = br.readLine().split(" ");
        int R = Integer.parseInt(RC[0]), C = Integer.parseInt(RC[1]);

        M = new char[R][C];
        N = new int[R][C];
        names = new ArrayList<String>(); names.add("");
        cities = new ArrayList<int[]>(); cities.add(new int[]{0, 0});

        for (int i = 0; i < R; ++i) {

            if (check) {
                check = false;
                names.add(temp);
                temp = "";
            }

            String line = br.readLine();
            for (int j = 0; j < C; ++j) {
                char c = line.charAt(j);
                M[i][j] = c;

                if (c == '.') {
                    if (check) {
                        check = false;
                        names.add(temp);
                        temp = "";
                    }
                }
                else if (c == 'x') {
                    if (check) {
                        check = false;
                        names.add(temp);
                        temp = "";
                    }
                    cities.add(new int[]{i, j});
                    ++cities_num;
                }
                else {
                    if (!check) {
                        check = true;
                        ++names_num;
                    }

                    temp += c;
                    N[i][j] = names_num;
                }
            }
        }
        if (temp != "") {
            names.add(temp);
            temp = "";
        }

        G = new ArrayList<>();
        for (int i = 0; i < cities_num+1; ++i) {
            G.add(new ArrayList<Integer>());
        }

        for (int i = 1; i < cities_num+1; ++i) {
            for (int[] d : delta) {
                int x = cities.get(i)[0] + d[0];
                int y = cities.get(i)[1] + d[1];

                if (x >= 0 && x < R && y >= 0 && y < C && N[x][y] != 0 && !G.get(i).contains(N[x][y])) {
                    G.get(i).add(N[x][y]);
                }
            }
        }

        F = new int[names_num+1];
        for (int i = 1; i < cities_num+1; ++i) {
            V = new int[names_num+1];
            B(i);
        }

        for (int i = 1; i < names_num+1; ++i) {
            System.out.print(cities.get(F[i])[0]+1);
            System.out.print(" ");
            System.out.print(cities.get(F[i])[1]+1);
            System.out.print(" ");
            System.out.println(names.get(i));
        }
    }
}