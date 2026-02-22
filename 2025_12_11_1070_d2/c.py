import sys
sys.setrecursionlimit(2500)

from typing import List

def odd(n: int, arr: List[int]) -> List[int]:
  #print(f"turns: {n}, cards: {arr}")
  odds = []
  evens = []
  for i in range(n):
    if arr[i] % 2 == 1:
      odds.append(arr[i])
    else:
      evens.append(arr[i])
  
  odds = sorted(odds, reverse=True)
  evens = sorted(evens, reverse=True)

  print(f"odds={odds}, evens={evens}")
  odds_count = len(odds)
  evens_count = len(evens)

  if odds_count == 0:
    return [0] * n
  
  if evens_count == 0:
    result = []
    for i in range(n):
      if i % 2 == 0:
        result.append(odds[0])
      else:
        result.append(0)
    return result

  #at least 1 odd and 1 even
  result = [odds[0]]
  for i in range(evens_count):
    result.append(result[i] + evens[i])
  
  #all good before this
  #two cases, start from odd or even index

  for i in range(evens_count + 1, n):
    if i % 2 == 1:
      result.append(result[evens_count-1])
    else:
      result.append(result[evens_count])


  return result

def main():
  lines = sys.stdin.read().strip().splitlines()
  t = int(lines[0])

  curr_line = 1
  for _ in range(t):
    n = int(lines[curr_line])
    curr_line += 1
    row = list(map(int, lines[curr_line].split()))
    curr_line += 1
    print(odd(n, row))

if __name__ == "__main__":
  main()
