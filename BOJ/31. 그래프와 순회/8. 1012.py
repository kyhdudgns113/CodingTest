#
# t : 테스트 케이스 개수
# m : 배추밭의 가로 길이
# n : 배추밭의 세로 길이
# k : 배추밭에 심어진 배추 갯수
#
# 상황
#   배추밭에 해충을 잡아먹는 지렁이를 배치하려 한다.
#   지렁이는 배추가 있는 가로세로 1칸으로만 이동한다.
#
# 구하는것
#   필요한 지렁이 수
#
# 풀이
#   dfs, bfs 전부 가능하다.
#   각 점에 대하여 방문한 적 없으면 dfs 를 수행하고 결과값을 1 늘린다.

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

t = int(input())

def dfs(isVisit, field, m, n, row, col):
  isVisit[row][col] = 1
  
  if row > 0 and field[row - 1][col] == 1 and isVisit[row - 1][col] == 0:
    dfs(isVisit, field, m, n, row - 1, col)
  if col > 0 and field[row][col - 1] == 1 and isVisit[row][col - 1] == 0:
    dfs(isVisit, field, m, n, row, col - 1)
  if row < m - 1 and field[row + 1][col] == 1 and isVisit[row + 1][col] == 0:
    dfs(isVisit, field, m, n, row + 1, col)
  if col < n - 1 and field[row][col + 1] == 1 and isVisit[row][col + 1] == 0:
    dfs(isVisit, field, m, n, row, col + 1)

for tt in range(t):
  m, n, k = map(int, input().split())
  field = [[0 for i in range(n)] for j in range(m)]
  for kk in range(k):
    r, c = map(int, input().split())
    field[r][c] = 1
  
  isVisit = [[0 for i in range(n)] for j in range(m)]
  result = 0
  
  for row in range(m):
    for col in range(n):
      if field[row][col] == 1 and isVisit[row][col] == 0:
        dfs(isVisit, field, m, n, row, col)
        result += 1
        
  print(result)
  