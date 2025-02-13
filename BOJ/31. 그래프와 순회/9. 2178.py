# n : 미로의 세로 길이
# m : 미로의 가로 길이
# field[][] : 해당 칸이 길이면 1, 벽이면 0
#
# 상황
#   0, 0 에서 시작하여 n - 1, m - 1 까지 가려 한다.
#
# 구하는것
#   최단거리
#
# 풀이
#   dfs 로는 풀기 힘들다.
#     dfs 로는 목표지점까지 최단거리로 이동하는 효율적인 알고리즘을 짤 수 없다.
#     도착지점까지 가는 모든 경우의 수를 세야 한다.
#     100*100 칸이 전부 1로 채워져있으면 경우의 수는 2^100 이다.
#       nCr 을 구하는것을 생각하면 경우의 수를 셀 수 있다.
#     시간초과가 난다.
#   bfs 로는 풀 수 있다.
#     bfs 인자로 해당 칸을 몇 번째로 밟았는지를 넘겨준다.
#     한 번 밟은칸은 bfs 로 방문하지 않는다.
#     도착지점에 도달할때 전달받은 거리가 최소거리가 된다.

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(input().strip()) for i in range(n)]

isVisit = [[0 for i in range(m)] for j in range(n)]
nextQueue = deque()
result = 0

def bfs(row, col, nowLen):
  global n, m, result
  isVisit[row][col] = 1
  if row == n - 1 and col == m - 1:
    result = nowLen
    return 0
  
  if row > 0 and isVisit[row - 1][col] == 0 and field[row - 1][col] == "1":
    nextQueue.append({'row': row - 1, 'col': col, 'nowLen': nowLen + 1})
  if col > 0 and isVisit[row][col - 1] == 0 and field[row][col - 1] == "1":
    nextQueue.append({'row': row, 'col': col - 1, 'nowLen': nowLen + 1})
  if row < n - 1 and isVisit[row + 1][col] == 0 and field[row + 1][col] == "1":
    nextQueue.append({'row': row + 1, 'col': col, 'nowLen': nowLen + 1})
  if col < m - 1 and isVisit[row][col + 1] == 0 and field[row][col + 1] == "1":
    nextQueue.append({'row': row, 'col': col + 1, 'nowLen': nowLen + 1})
    
  while len(nextQueue) > 0:
    elem = nextQueue.popleft()
    if isVisit[elem['row']][elem['col']] == 0:
      return bfs(elem['row'], elem['col'], elem['nowLen'])
  
  return 0

bfs(0, 0, 1)

print(result)
    