import sys

class B:
  def __init__(self):
    return

  def solve(self, m, l, r):
    if m <= -l:
      return [-m, 0]
    elif m <= r:
      return [0, m]
    else:
      return [l, l+m]


solver = B()
t = int(input())

for i in range(t):
  line = input()
  line = line.strip().split()
  inputs = list(map(lambda x: int(x), line))

  val = solver.solve(inputs[1], inputs[2], inputs[3])
  print(f"{val[0]} {val[1]}")

