import java.io.*;
import java.util.*;

public class ModularExponentiation {
    public static void main(String[] args) {
        int[] inputs = readInputs();

        String exponents = intToBinary(inputs[1]);
        System.out.println(exponents);

        int remainder = 1;
        long base = inputs[0];
        for (int i = exponents.length() - 1; i >= 0; i--) {
            if (i != exponents.length() - 1)
                base *= base;

            if (exponents.charAt(i) == '1') {
                int temp = (int) base % inputs[2];
                System.out.println(temp);
                remainder *= temp;
            }
        }

        int res = remainder % inputs[2];
        System.out.println(res);
    }

    private static int[] readInputs() {
        int[] inputs = new int[3];

        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        String[] temp = str.split(" ");
        in.close();

        for (int i = 0; i < 3; i++)
            inputs[i] = Integer.valueOf(temp[i]);

        return inputs;
    }

    private static String intToBinary(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            if (n % 2 == 0)
                sb.append("0");
            else
                sb.append("1");
            n /= 2;
        }
        return sb.reverse().toString();
    }
}