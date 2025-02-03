import sys

w = list(list(list(0 for i in range(21)) for j in range(21)) for k in range(21))

def func(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  
  if a > 20 or b > 20 or c > 20:
    return func(20, 20, 20)
  
  if w[a][b][c] != 0:
    return w[a][b][c]
  
  if a < b and b < c:
    w[a][b][c] = func(a, b, c - 1) + func(a, b - 1, c - 1) - func(a, b - 1, c)
  
  else:
    w[a][b][c] = func(a - 1, b, c) + func(a - 1, b - 1, c) + func(a - 1, b, c - 1) - func(a - 1, b - 1, c - 1)
    
  return w[a][b][c]

input = sys.stdin.readline
output = sys.stdout.write
while True:
  a, b, c = map(int, input().split())
  if a == -1 and b == -1 and c == -1:
    break
  
  output("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(func(a, b, c)) + '\n')
  
  