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
        System.out.println(minCoinsTillIndex(n, 4));
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

  private static int minCoinsTillIndex(int n, int i) {
    if (n <= 1) return n;
    if (i == 0) return n;
    if (i == 1) return (n/c[1]) + minCoinsTillIndex(n % c[1], 0);
    if (i == 2) return (n/c[2]) + minCoinsTillIndex(n % c[2], 1);

    System.out.println(String.format("for %d using %d", n, i));
    int numTimes = n / c[i];
    int amountLeft = n % c[i];
    int min, next;
    min = n;
    amountLeft = n % c[i];

    for (int j = numTimes; j >= 0; j--) {
      next = j + minCoinsTillIndex(amountLeft, i-1);
      amountLeft += c[i];
      min = min > next ? next : min;
    }
    return min;
  }
}
