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
        Map<Integer, Set<Integer> > m = new HashMap<>();
        for (int j = 0; j < n-1; j++) {
          String[] shape = reader.readLine().split("\\s+");
          int u = Integer.parseInt(shape[0]);
          int v = Integer.parseInt(shape[1]);
          m.putIfAbsent(u, new Set<Integer>());
          m.putIfAbsent(v, new Set<Integer>());
          m.get(u).add(v);
          m.get(v).add(u);
          System.out.println(minDelete(m, n));
        }
      }
      reader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static void findLongest(Map<Integer, Set<Integer>> m, int n, List<Integer> p) {
    Set<Integer> s = m.keySet();
    Iterator<Integer> it = s.iterator();
    int start = it.next();

    p.clear();
    int newStart = dfs(m, p, start, n);
    p.clear();
    dfs(m, p, newStart, n);
  }

  public static int dfs(Map<Integer, Set<Integer>> m, List<Integer> p, int start, int n) {
    boolean[] visited = new visited[n];
    for (int i = 0; i < n; i++) visited[i] = false;

    return dfsHelper(m, p, start, n, visited, 0);
  }

  public static int dfsHelper(Map<Integer, Set<Integer>> m, List<Integer> p, int start, int n, boolean[] visited, int dist, List<Integer> longest) {
    if (!m.containsKey(start)) return 0;

    if (dist > longest.size()) {
      longest = new List<Integer>();
      longest.addAll(p);
    }
    Set<Integer> s = m.get(start);
    Iterator<Integer> it = s.iterator();

    while(it.hasNext()) {
      int v = it.next();
      if (visited[v]) continue;
      visited[v] = true;
      p.add(v);
      dfsHelper(m, p, v, n, visited, dist+1);
      p.remove(p.size()-1);
      visited[v] = false;
    }
  }

  public static int minDelete(Map<Integer, Set<Integer>> m, int n) {

    int dels = 0;
    while(m.size() > 1) {
      dels++;
      //get longest path into path
      List<Integer> p = new ArrayList<>();
      findLongest(m, n, p);
      int keep = p.get(0);
      for (int i = 1; i < p.size(); i++) {
        Set<Integer> edgesFromI = m.get(p.get(i));
        Iterator<Integer> it = edgesFromI.iterator();
        while (it.hasNext()) {
          int v = it.next();
          if (m.containsKey(v)) {
            m.get(keep).add(v);
            m.get(v).add(keep);
          }
        }
        m.remove(p.get(i));
      }
      return dels;
    //traverse along path and remove all but the first node in it from map
    //and add all the edges that still exist into that node
    //continue this until 1 vertex is left
    //return number of deletions.
    }

  }
}
