import sys
sys.setrecursionlimit(2500)

class D:
  def __init__(self, p, s, m, n):
    self.p = p
    self.s = s
    self.m = m
    self.n = n

  def solve(self, p_pos, s_pos):
    if p_pos == self.m and s_pos == self.n:
      return True
    else:
      if p_pos == self.m or s_pos == self.n:
        return False

    hit = self.p[p_pos]
    if self.s[s_pos] != hit:
      return False

    if self.solve(p_pos + 1, s_pos + 1):
      return True

    if s_pos < (n-1) and s[s_pos+1] == hit:
      return self.solve(p_pos + 1, s_pos + 2)


t = int(input())
for i in range(t):
  p = input().strip()
  s = input().strip()

  m = len(p)
  n = len(s)
  solver = D(p, s, m, n)

  canSound = solver.solve(0, 0)
  if canSound:
    print("YES")
  else:
    print("NO")
