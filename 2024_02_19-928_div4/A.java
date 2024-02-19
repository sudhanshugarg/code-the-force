import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class A {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(reader.readLine());
      int A, B;
      for (int i = 0; i < n; i++) {
        A = B = 0;
        String vlad = reader.readLine();
        for (int j = 0; j < vlad.length(); j++) {
          if (vlad.charAt(j) == 'A') A++;
          else B++;
        }
        if (A > B) System.out.println("A");
        else System.out.println("B");
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
