# n : 점의 갯수
# m : 간선의 갯수
# r : 시작점의 숫자
# inp[] : (시작점, 끝점) 으로 구성된 간선들의 배열
#
# 상황
#   모든 i 에 대하여 inp[i] 를 내림차순으로 정렬한다.
#   r 에서부터 bfs 를 한다.
#   방문한 순서를 기록한다.
#
# 구하는것
#   각 점들이 방문한 순서를 출력한다.
#   방문한 적 없으면 0 을 출력한다.

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
output = sys.stdout.write

n, m, r = map(int, input().split())
inp = [list(map(int, input().split())) for i in range(m)]

info = [[] for i in range(n + 1)]

for elem in inp:
  u, v = elem
  info[u].append(v)
  info[v].append(u)
  
for i in range(1, n + 1):
  info[i].sort()
  info[i].reverse()

isVisit = [0 for i in range(n + 1)]
visitCnt = 1
nextQueue = deque()

def bfs(start):
  global visitCnt
  isVisit[start] = visitCnt
  visitCnt += 1
  
  for next in info[start]:
    if isVisit[next] == 0:
      nextQueue.append(next)
  
  while len(nextQueue) > 0:
    next = nextQueue.popleft()
    if isVisit[next] == 0:
      return bfs(next)
    
  return 0

bfs(r)

for num in range(1, n + 1):
  output(str(isVisit[num]) + '\n')
