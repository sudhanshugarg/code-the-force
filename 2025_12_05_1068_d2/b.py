import sys
sys.setrecursionlimit(2500)

from typing import List

def tactical(turns: int, cards: List[List[int]]) -> None:
  #print(f"turns: {turns}, cards: {cards}")

  least: List[int] = [0] * (turns+1)
  highest: List[int] = [0] * (turns+1)

  for i in range(turns):
    #next = (cards[0][i] + cards[1][i]) / 2.0
    # choose
    val1 = least[i] - cards[0][i]
    val2 = cards[1][i] - least[i]
    val3 = highest[i] - cards[0][i]
    val4 = cards[1][i] - highest[i]

    least[i+1] = min(val1, val2, val3, val4)
    highest[i+1] = max(val1, val2, val3, val4)

  print(highest[turns])


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
