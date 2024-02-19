import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class D {
  public static void main(String[] args) {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      int t = Integer.parseInt(reader.readLine());
      int n;
      for (int i = 0; i < t; i++) {
        n = Integer.parseInt(reader.readLine());
        DivisionD s = new DivisionD(reader.readLine());
        System.out.println(s.group());
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}

class DivisionD {
  private int[] nums;
  private Map<Integer, Integer> freq;
  private static int two31 = (1 << 31) - 1;

  DivisionD(String s) {
    String[] s2 = s.split("\\s+");
    nums = new int[s2.length];
    freq = new HashMap<>();
    for (int i = 0; i < s2.length; i++) {
      nums[i] = Integer.parseInt(s2[i]);
      if (!freq.containsKey(nums[i])) {
        freq.put(nums[i], 0);
      }
      freq.put(nums[i], freq.get(nums[i]) + 1);
    }
  }

  public int group() {
    int g = 0;
    int inv;
    int ct1, ct2;
    for (int i = 0; i < nums.length; i++) {
      ct1 = freq.getOrDefault(nums[i], 0);
      if (ct1 == 0) continue;
      freq.put(nums[i], freq.get(nums[i]) - 1);
      g++;

      inv = two31 - nums[i];
      //System.out.println(String.format("%d, %d", nums[i], inv));
      ct2 = freq.getOrDefault(inv, 0);
      if (ct2 > 0) {
        freq.put(inv, freq.get(inv) - 1);
      }
    }
    return g;
  }
}
