import java.util.Scanner;
public class Armstrong {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), sum = 0, temp = n;

        while (n > 0) {
            int d = n % 10;
            sum += d * d * d;
            n /= 10;
        }

        if (sum == temp)
            System.out.println("Armstrong");
        else
            System.out.println("Not Armstrong");
    }
}
