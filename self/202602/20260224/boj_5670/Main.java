import java.io.*;
import java.util.*;


class Main {

    static class Node {
        int[] child = new int[26];
        boolean isEnd;
        int childCount;

        Node() {
            Arrays.fill(child, -1);
            isEnd = false;
            childCount = 0;
        }
    }

    static int N;
    static ArrayList<Node> trie = new ArrayList<>();
    static ArrayList<String> words = new ArrayList<>();

    static void solve(BufferedReader br) throws IOException {
        trie.clear();
        words.clear();

        trie.add(new Node());

        for (int i = 0; i < N; ++i) {
            String s = br.readLine();
            words.add(s);

            int cur = 0;
            for (int idx = 0; idx < s.length(); ++idx) {
                int c = s.charAt(idx) - 'a';

                if (trie.get(cur).child[c] == -1) {
                    trie.get(cur).child[c] = trie.size();
                    trie.add(new Node());
                    ++trie.get(cur).childCount;
                }

                cur = trie.get(cur).child[c];
            }

            trie.get(cur).isEnd = true;
        }

        float ans = 0;

        for (String word : words) {
            int cnt = 1;
            int cur = 0;

            int first = word.charAt(0) - 'a';
            cur = trie.get(cur).child[first];

            for (int i = 1; i < word.length(); ++i) {
                if (trie.get(cur).childCount > 1 || trie.get(cur).isEnd) ++cnt;

                int c = word.charAt(i) - 'a';
                cur = trie.get(cur).child[c];
            }

            ans += cnt;
        }

        System.out.printf(Locale.US, "%.2f%n", ans/N);

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while ((line = br.readLine()) != null) {
            N = Integer.parseInt(line);
            solve(br);
        }

        return;
    }
}
