import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int k = Integer.parseInt(reader.readLine());
      for (int i = 0; i < k; i++) {
        int len = Integer.parseInt(reader.readLine());
        String s = reader.readLine();
        int ans = 0;
        for (int j = 0; j < s.length(); j++) {
          if (s.charAt(j) == '+') ans++;
          else ans--;
        }
        System.out.println(Math.abs(ans));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
