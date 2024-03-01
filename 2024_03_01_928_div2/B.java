import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(reader.readLine());
      for (int i = 0; i < t; i++) {
        int n = Integer.parseInt(reader.readLine());
        System.out.flush();
        System.out.println(minCoinsMain(n));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static int[] c = {1,3,6,10,15};
  private static int minCoins(int n) {
    int[] amount;
    if (n < 15) {
      amount = new int[16];
    }
    else {
      amount = new int[n+1];
    }

    amount[0] = 0;
    for (int i = 0; i < c.length; i++)
      amount[c[i]] = 1;

    int min, next;
    for (int i = 2; i <= n; i++) {
      if (amount[i] > 0) continue;
      amount[i] = Integer.MAX_VALUE;
      for (int j = 0; j < c.length; j++) {
        if (i < c[j]) break;
        if (amount[i-c[j]] > 0) {
          next = 1 + amount[i - c[j]];
          amount[i] = amount[i] > next ? next : amount[i];
        }
      }
    }
    return amount[n];
  }

  private static int minCoinsMain(int n) {
    int c15 = n / 15;
    int min, next;
    min = c15 + minCoins15(n % 15);
    for (int i = c15 - 1, j = 1; i >= 0; i--, j++) {
      n -= 15;
      next = j + minCoins15(n);
      System.out.println(String.format("%d, %d, %d", n, j, next));
      min = min > next ? next : min;
    }
    return min;
  }

  private static int minCoins15(int n) {
    if (n <= 15) return minCoins(n);
    int c15 = n / 15;
    return c15 + minCoins(n % 15);
  }
}
