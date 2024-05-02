import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            String[] data = new String[n];

            int count = 0;
            for (String item: data) {
                int con = 0;
                int a1 = scanner.nextInt();
                int a2 = scanner.nextInt();
                int a3 = scanner.nextInt();
              
                if (a1 == 1) con++;
                if (a2 == 1) con++;
                if (a3 == 1) con++;

                if (con > 1) count++;
            }
            System.out.print(count);
        }
    }
}
