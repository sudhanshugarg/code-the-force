import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class E {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(reader.readLine());
      int n, k;
      for (int i = 0; i < t; i++) {
        CardsE s = new CardsE(reader.readLine());
        System.out.println(s.which());
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}

class CardsE {
  private int n;
  private int kth;

  CardsE(String s) {
    String[] s2 = s.split("\\s+");
    n = Integer.parseInt(s2[0]);
    kth = Integer.parseInt(s2[1]);
  }

  public int which() {
    //System.out.println(String.format("n=%d, k=%d", n, kth));
    int powerof2 = 2;
    int k = kth;
    int oddNumbers, highestOddNumber, multiplier;
    while(k > 0) {
      multiplier = powerof2 / 2;
      oddNumbers = n / powerof2;
      highestOddNumber = 2 * (oddNumbers - 1) + 1;
      while(multiplier * (highestOddNumber + 2) <= n) {
        highestOddNumber += 2;
        oddNumbers++;
      }
      //System.out.println(String.format("multiplier=%d, oddNumbers=%d, highestOddNumber=%d, k=%d", multiplier, oddNumbers, highestOddNumber, k));

      if (k <= oddNumbers) {
        //found it
        return multiplier * (2 * (k-1) + 1);
      } else {
        k -= oddNumbers;
        powerof2 *= 2;
      }
    }
    return 0;
  }
}
