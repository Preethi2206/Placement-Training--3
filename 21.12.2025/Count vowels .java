import java.util.Scanner;
public class VowelCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int count = 0;

        for (char c : s.toLowerCase().toCharArray()) {
            if ("aeiou".indexOf(c) != -1)
                count++;
        }

        System.out.println("Vowels: " + count);
    }
}
