import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class A {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(reader.readLine());
      int x;
      for (int i = 0; i < t; i++) {
        int n = Integer.parseInt(reader.readLine());
        String[] arrStr = reader.readLine().split("\\s+");
        int[] arr = new int[n];
        for (int j = 0; j < n; j++) {
          arr[j] = Integer.parseInt(arrStr[j]);
        }
        System.out.println(maxAbsSum(arr, n));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static int maxAbsSum(int[] arr, int n) {
    Arrays.sort(arr);
    int a = 2 * (arr[n-1] - arr[0]);
    int b = 2 * (arr[n-1] + arr[n-2] - arr[0] - arr[1]);
    return a < b ? b : a;
  }
}
