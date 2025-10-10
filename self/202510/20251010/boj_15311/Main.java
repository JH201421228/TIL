import java.io.*;
import java.util.*;


public class Main {
    static String ans = "1999\n";


    public static void main(String[] args) throws IOException {
        for (int i = 0; i < 999; ++i) ans += "1 ";
        for (int i = 0; i < 1000; ++i) ans += "1000 ";

        System.out.println(ans);

        return;
    }
}
