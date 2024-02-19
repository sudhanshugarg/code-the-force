import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class C {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(reader.readLine());
      int n;
      for (int i = 0; i < t; i++) {
        n = Integer.parseInt(reader.readLine());
        System.out.println(sumDigits(n));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  
  private static int sumDigits(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
      total += sumDig(i);
    }
    return total;
  }

  private static int sumDig(int n) {
    int ct = 0;
    while(n > 0) {
      ct += n % 10;
      n /= 10;
    }
    return ct;
  }

  private static int sumDigits2(int n) {
    int d = 0;
    int x = n;
    while(x > 9) {
      x /= 10;
      d++;
    }

    int total = 0;
    for (int i = 1; i <= d; i++) {
      total += sumWithDigits(9, i);
    }
    total += sumWithDigits(x, d+1);
    return total;
  }

  private static int sumWithDigits(int firstDigitLimit, int numDigits) {
    return 0;
  }
}
