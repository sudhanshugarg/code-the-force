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
        String[] arrStr = reader.readLine().split("\\s+");
        int[] arr = new int[arrStr.length];
        for (int j = 0; j < arrStr.length; j++) {
          arr[j] = Integer.parseInt(arrStr[j]);
        }
        System.out.println(penalty(arr));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static int penalty(int[] arr) {
    int[] prev = new int[arr.length];
    int[] len = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
      prev[i] = i;
      len[i] = 1;
    }

    for (int i = 1; i < arr.length; i++) {
      

    }
  }
}
