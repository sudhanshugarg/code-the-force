import sys
sys.setrecursionlimit(2500)

from typing import List

def inversions(n: int, arr: List[int]) -> int:
  #print(f"turns: {n}, cards: {arr}")
  removed = 0

  maxSoFar = arr[0]
  for i in range(1, n):
    if arr[i] < maxSoFar:
      removed += 1
    else:
      maxSoFar = arr[i]

  return removed

def main():
  lines = sys.stdin.read().strip().splitlines()
  t = int(lines[0])

  curr_line = 1
  for _ in range(t):
    n = int(lines[curr_line])
    curr_line += 1
    row = list(map(int, lines[curr_line].split()))
    curr_line += 1

    print(inversions(n, row))

if __name__ == "__main__":
  main()
