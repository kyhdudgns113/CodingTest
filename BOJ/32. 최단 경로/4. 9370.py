#
# n : 점의 개수
# m : 간선의 갯수
# t : 체크할 점의 개수
#
# s : 시작하는 점의 번호
# g, h : 지나쳐야하는 간선의 양 끝 점
#
# candidates[] : 체크할 점의 목록
#
# 상황
#   s 에서 시작해서 모든 점에 대하여 각각 최단거리로 간다
#
# 구하는것
#   candidates 에 있는 점으로 가는 최단경로에 대하여
#   간선 (g, h) 를 지나는 것들만 출력
#
# 풀이
#   한 점에서의 최단경로와 관련된 문제기에 다익스트라를 쓸 수 있다.
#   한 점에 도착했을때 (g, h) 를 지나쳤는지 정보도 저장한다.
#     이 점에서 다음 점들을 확인할때 g, h 를 지나는지 확인한다.

from queue import PriorityQueue
import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for TT in range(T):
  n, m, t = map(int, input().split())
  s, g, h = map(int, input().split())
  
  connections = [[] for i in range(n + 1)]
  for mm in range(m):
    a, b, d = map(int, input().split())
    connections[a].append([b, d])
    connections[b].append([a, d])
    
  candidates = [int(input()) for i in range(t)]
  candidates.sort()
  
  nextVisit = PriorityQueue()  
  isMediate = [0 for i in range(n + 1)]
  distances = [10 ** 9 for i in range(n + 1)]
  distances[s] = 0
  
  for connection in connections[s]:
    dest, dist = connection
    
    mediate = 0
    if s == g and dest == h or s == h and dest == g:
      mediate = -1
    
    nextVisit.put([dist, dest, mediate])
    
  while nextVisit.qsize() > 0:
    dist, now, mediate = nextVisit.get()
    
    if distances[now] != 10 ** 9:
      continue
    
    for connection in connections[now]:
      dest, dist1 = connection
      if distances[dest] == 10 ** 9:
        medi = mediate
        if (now == g and dest == h) or (now == h and dest == g):
          medi = -1
        
        nextVisit.put([dist + dist1, dest, medi])
    distances[now] = dist
    isMediate[now] = mediate
  
  for candy in candidates:
    if isMediate[candy] == -1:
      output(str(candy) + ' ')
  output('\n')
        
  