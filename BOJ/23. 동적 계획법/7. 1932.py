# 
# triangle[row][col] = row 번째 줄의 col 번째 값
# results[row][col] = 
#   max(
#     results[row - 1][col - 1] : 왼쪽 위에서 내려오는 경우
#    ,results[row - 1][col] : 오른쪽 위에서 내려오는 경우
#   ) + triangle[row][col]

import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
triangle = []
results = [[0 for i in range(n)] for j in range(n)]

for _ in range(n):
  triangle.append(list(map(int, input().split())))

results[0][0] = triangle[0][0]

for i in range(1, n):
  for j in range(i + 1):
    tempMax = results[i - 1][j]
    if j > 0:
      tempMax = max(tempMax, results[i - 1][j - 1])
    results[i][j] = tempMax + triangle[i][j]
    
if n > 1:
  print(max(*results[n - 1]))
else:
  print(results[0][0])