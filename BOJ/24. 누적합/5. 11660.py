#
# 문제 : n * n 행렬 chart가 주어진다. (n <= 1024)
#       chart(x1, y1) 부터 chart(x2, y2) (x1 < x2, y1 < y2) 까지의 합을
#       m 번 구하여라 (m <= 100000)
#
# n : 행렬 한 변의 길이
# m : 답을 구하는 횟수
# chart[][] : 행렬
#
# sumsMatrix[row][col] : chart[0][0] 부터 chart[row][col] 까지의 합
# 
# inner = chart[0][0] 부터 chart[x1 - 1][y1 - 1] 까지의 합
# upper = chart[0][0] 부터 chart[x1 - 1][y2] 까지의 합
# left = chart[0][0] 부터 chart[x2][y1 - 1] 까지의 합합
# entire = chart[0][0] 부터 chart[x2][y2] 까지의 합합
#
# chart[x1][y1] 부터 chart[x2][y2] 까지의 합
#   = entire - upper - left + inner
#   = sumsMatrix[x2][y2] - sumsMatrix[x1 - 1][y2]
#     - sumsMatrix[x2][y1 - 1] + sumsMatrix[x1 - 1][y1 - 1]
#
# 여기서 sumsMatrix 를 구하는 점화식은 다음과 같다.
#
# sumsMatrix[row][col] = 
#     sumsMatrix[row - 1][col]
#   + sumsMatrix[row][col - 1]
#   + chart[row][col]
#
# 위 두 점화식을 인덱스가 벗어나는 경우등을 잘 고려하여 구현하면 다음과 같다.
#   

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

chart = list(list(map(int, input().split())) for i in range(n))

sumsMatrix = [[0 for i in range(n)] for j in range(n)]

def sums(r, c):
  if r < 0 or c < 0:
    return 0
  
  if sumsMatrix[r][c] > 0:
    return sumsMatrix[r][c]
  
  inner = sums(r - 1, c - 1) if r > 0 and c > 0 else 0
  upper = sums(r - 1, c) if r > 0 else 0
  left = sums(r, c - 1) if c > 0 else 0
  
  sumsMatrix[r][c] = upper + left - inner + chart[r][c]
  return sumsMatrix[r][c]

sums(n - 1, n - 1)

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  inner = sumsMatrix[x1 - 2][y1 - 2] if x1 > 1 and y1 > 1 else 0
  upper = sumsMatrix[x1 - 2][y2 - 1] if x1 > 1 else 0
  left = sumsMatrix[x2 - 1][y1 - 2] if y1 > 1 else 0
  
  result = sumsMatrix[x2 - 1][y2 - 1] - upper - left  + inner
  output(str(result) + '\n')
  