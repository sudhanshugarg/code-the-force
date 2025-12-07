import sys
sys.setrecursionlimit(2500)

from typing import List

def tactical(turns: int, cards: List[List[int]]) -> int:
  print(f"turns: {turns}, cards: {cards}")
  return 0

def main():
  lines = sys.stdin.read().strip().splitlines()
  t = int(lines[0])

  curr_line = 1
  for _ in range(t):
    n = int(lines[curr_line])
    curr_line += 1
    rows: list[list[int]] = []
    for _ in range(2):
      row = list(map(int, lines[curr_line].split()))
      rows.append(row)
      curr_line += 1

    tactical(n, rows)

if __name__ == "__main__":
  main()
