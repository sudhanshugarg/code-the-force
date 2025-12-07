import sys
sys.setrecursionlimit(2500)

from typing import List

def kanades_perfect_multiples(n: int, k: int, arr: List[int]) -> None:
  #print(f"n={n}, k={k}, arr={arr}")

  #sort arr
  #create a set of not_visited
  #put smallest item into b
  #remove all multiples of b from not_visited
  #take next smallest and add to b
  #keep doing until not_visited is empty

  not_covered = set(arr)
  elements = not_covered.copy()
  arr = sorted(arr)

  perfect: List[int] = []
  for b in arr:
    if b not in not_covered:
      continue

    not_covered.remove(b)

    #check if all multiples of b are in elements
    mult = 2 * b
    while mult <= k:
      if mult not in elements:
        print(-1)
        return
      if mult in not_covered:
        not_covered.remove(mult)
      mult += b

    perfect.append(b)

  print(len(perfect))
  print(" ".join(map(str, perfect)))


def main():
  lines = sys.stdin.read().strip().splitlines()
  t = int(lines[0])

  curr_line = 1
  for _ in range(t):
    n, k = map(int, lines[curr_line].split())
    curr_line += 1
    row = list(map(int, lines[curr_line].split()))
    kanades_perfect_multiples(n, k, row)
    curr_line += 1
    

if __name__ == "__main__":
  main()