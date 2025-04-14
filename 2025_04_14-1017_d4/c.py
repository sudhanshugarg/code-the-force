t = int(input())
for i in range(t):
  n = int(input())
  permutation = []
  first_element = n * (2 * n + 1)
  for j in range(n):
    rowStr = input().strip().split()
    if j == n-1:
      row = list(map(lambda x: int(x), rowStr))
      for k in row:
        first_element -= k
      permutation.extend(row)
    else:
      next_elem = int(rowStr[0])
      permutation.append(next_elem)
      first_element -= next_elem

  print(first_element, end="")
  for j in permutation:
    print(f" {j}", end="")
  print("")
