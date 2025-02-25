#
# V : 점의 갯수
# E : 간선의 갯수
# inp[] : (A, B, 거리) 로 이루어진 배열. A 와 B 사이가 "거리" 만큼 걸린다는 뜻이다.
#
# 상황
#   모든 점들을 연결하려고 한다.
#
# 구하는것
#   모든 점을 연결하는데 필요한 최소 거리
#
# 풀이
#   최소 신장 트리 알고리즘을 이용하면 구할 수 있다.

from queue import PriorityQueue
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

connections = [[] for i in range(V + 1)]

for ee in range(E):
  a, b, c = map(int, input().split())
  connections[a].append([c, b])
  connections[b].append([c, a])
  
nextVisit = PriorityQueue()
nextVisit.put([0, 1])

isVisit = [0 for i in range(V + 1)]
result = 0

while nextVisit.qsize() > 0:
  dist, now = nextVisit.get()
  
  if isVisit[now] != 0:
    continue
  
  for connection in connections[now]:
    dist0, next = connection
    if isVisit[next] == 0:
      nextVisit.put([dist0, next])
    
  isVisit[now] = 1
  result += dist
  
print(result)
  
