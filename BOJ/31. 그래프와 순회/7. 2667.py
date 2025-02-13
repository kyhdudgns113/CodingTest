# n : 정사각형 한 변의 길이
# mapArr[][] : 0 아니면 1이 채워져있는 n * n 행렬
#
# 상황
#   상하좌우로 연결되어있는 1 들은 하나의 집을 형성한다.
#   대각선은 고려하지 않는다.
#
# 구하는것
#   집의 갯수
#   집들의 크기를 오름차순으로 구한것
#
# 풀이
#   dfs, bfs 둘 다 가능하다.
#   dfs 가 코드가 더 간단하여 이것으로 구현하였다.

import sys

input = sys.stdin.readline

n = int(input())
mapArr = [list(input().strip()) for i in range(n)]

sizeArr = []
isVisit = [[0 for i in range(n)] for j in range(n)]

def dfs(row, col):
  global n
  isVisit[row][col] = 1
  
  ret = 1
  
  if row > 0 and mapArr[row - 1][col] == "1" and isVisit[row - 1][col] == 0:
    ret += dfs(row - 1, col)
  if col > 0 and mapArr[row][col - 1] == "1" and isVisit[row][col - 1] == 0:
    ret += dfs(row, col - 1)
  if row < n - 1 and mapArr[row + 1][col] == "1" and isVisit[row + 1][col] == 0:
    ret += dfs(row + 1, col)
  if col < n - 1 and mapArr[row][col + 1] == "1" and isVisit[row][col + 1] == 0:
    ret += dfs(row, col + 1)
  return ret

for row in range(n):
  for col in range(n):
    if isVisit[row][col] == 0 and mapArr[row][col] == "1":
      val = dfs(row, col)
      sizeArr.append(val)

sizeArr.sort()

print(len(sizeArr))

for num in sizeArr:
  print(num)