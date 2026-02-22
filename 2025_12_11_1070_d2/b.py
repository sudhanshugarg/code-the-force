import sys
sys.setrecursionlimit(2500)

from typing import List

def shifts(n: int, bin: str) -> int:
  #print(f"turns: {n}, cards: {bin}")
  last_one_index = -1
  max_dist_from_one = 0
  for i in range(n):
    if bin[i] == '1':
      last_one_index = i
    elif last_one_index != -1:
      moves = i - last_one_index
      max_dist_from_one = max(moves, max_dist_from_one)

  if last_one_index == -1:
    return 0
  
  for i in range(n):
    if bin[i] == '1':
      break

    #moves = #(last_one_index + x) % n = i, l + x = i, x = i - l
    moves = (i - last_one_index) % n
    max_dist_from_one = max(moves, max_dist_from_one)
 
  return max_dist_from_one    

def main():
  lines = sys.stdin.read().strip().splitlines()
  t = int(lines[0])

  curr_line = 1
  for _ in range(t):
    n = int(lines[curr_line])
    curr_line += 1
    bin = str(lines[curr_line])
    curr_line += 1

    print(shifts(n, bin))

if __name__ == "__main__":
  main()
