import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();

            String[] data = new String[n];

            for (int i = 0; i < n; i++) {
                data[i] = scanner.next();
                if (data[i].length() > 10)
                    data[i] = String.valueOf(data[i].charAt(0) + "" + (data[i].length() - 2) + "" + data[i].charAt(data[i].length() - 1));
            }

            for (String item : data)
                System.out.println(item);
        }
    }
}
