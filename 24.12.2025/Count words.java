import java.util.Scanner;
public class WordCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        String[] words = s.trim().split("\\s+");
        System.out.println("Words: " + words.length);
    }
}
