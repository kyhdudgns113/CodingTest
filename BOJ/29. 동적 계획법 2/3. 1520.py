#
# m, n : 지도의 세로, 가로 길이
# maps[][] : 지도에 적힌 수
#
# 상황
#   maps[0][0] 에서 시작한다.
#     상하좌우 어디던지 자기보다 낮은 숫자로 이동한다
#     maps[m - 1][n - 1] 까지 이동한다.
#
# 구하는것
#   이동하는 경우의 수
#
# 풀이
#   f(row, col) : row, col 까지 경로의 수
#   f(row, col) = sum(
#     위에서부터 내려오는 경우의수
#     왼쪽에서 오는 경우의 수
#     오른쪽에서 오는 경우의 수
#     아래에서 올라오는 경우의 수
#   )
#   이를 재귀함수로 풀면 된다


import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(m)]
numWays = [[-1 for i in range(n)] for j in range(m)]

def getNumWays(row, col):
  global m, n
  if row + col == 0:
    numWays[row][col] = 1
    return 1
  if numWays[row][col] != -1:
    return numWays[row][col]
  
  up = 0
  left = 0
  right = 0
  down = 0
  if row > 0 and maps[row - 1][col] > maps[row][col]:
    up = getNumWays(row - 1, col)
  if col > 0 and maps[row][col - 1] > maps[row][col]:
    left = getNumWays(row, col - 1)
  if row < m - 1 and maps[row + 1][col] > maps[row][col]:
    down = getNumWays(row + 1, col)
  if col < n - 1 and maps[row][col + 1] > maps[row][col]:
    right = getNumWays(row, col + 1)
  numWays[row][col] = up + left + down + right
  return numWays[row][col]

print(getNumWays(m - 1, n - 1))