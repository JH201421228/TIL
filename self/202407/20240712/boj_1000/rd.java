package boj_1000;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class rd {
    public static void main (String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();

        String[] numbers = line.split(" ");
        int sum = 0;

        for (String num : numbers) {
            sum += Integer.parseInt(num);
        }

        System.out.println(sum);
    }
}