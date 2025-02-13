#
# n : 점의 갯수
# m : 간선의 갯수
# v : 시작점의 번호
#
# 상황
#   한 점에서 한 점으로 이동할때, 가능하면 숫자가 낮은곳에 먼저 간다
#
# 구하는것
#   dfs 했을때 방문순서
#   bfs 했을때 방문순서

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
output= sys.stdout.write

n, m, v = map(int, input().split())
inps = [list(map(int, input().split())) for i in range(m)]

conn = [[] for i in range(n + 1)]

for inp in inps:
  a, b = inp
  conn[a].append(b)
  conn[b].append(a)

for i in range(1, n + 1):
  conn[i].sort()
  
isVisitDFS = [0 for i in range(n + 1)]
def dfs(now):
  isVisitDFS[now] = 1
  output(str(now) + ' ')
  
  for next in conn[now]:
    if isVisitDFS[next] == 0:
      dfs(next)

isVisitBFS = [0 for i in range(n + 1)]
nextQueue = deque()
def bfs(now):
  isVisitBFS[now] = 1
  output(str(now) + ' ')
  
  for next in conn[now]:
    if isVisitBFS[next] == 0:
      isVisitBFS[next] = 1
      nextQueue.append(next)
  
  while len(nextQueue) > 0:
    next = nextQueue.popleft()
    return bfs(next)
  return 0

dfs(v)
print()
bfs(v)
