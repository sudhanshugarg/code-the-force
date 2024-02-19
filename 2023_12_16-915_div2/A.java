import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class A {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int k = Integer.parseInt(reader.readLine());
      for (int i = 0; i < k; i++) {
        String[] shape = reader.readLine().split("\\s+");
        int m = Integer.parseInt(shape[0]);
        int n = Integer.parseInt(shape[1]);
        int output = m < n ? n : m;
        System.out.println(output);
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
