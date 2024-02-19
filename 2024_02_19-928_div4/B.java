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
        String[] grid = new String[n];
        for (int j = 0; j < n; j++) {
          String line = reader.readLine();
          grid[j] = line;
        }
        System.out.println(getShape(grid));
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }


  private static String getShape(String[] grid) {
    int n = grid.length;
    //go through lines and count 1s
    //just need 2 lines of 1s
    int ones = 0;
    int first = 0;
    for (int i = 0; i < n; i++) {
      ones = 0;
      for (int j = 0; j < n; j++) {
        if (grid[i].charAt(j) == '1') ones++;
      }
      if (ones == 0) continue;

      if (first == 0) {
        first = ones;
        continue;
      }

      if (ones == first) return "SQUARE";
      return "TRIANGLE";
    }
    return "NOTHING";
  }
}
