# n : 점의 갯수
# e : 양방향 간선의 갯수
# connections[start] = start 에서 출발하는 간선정보 (end, distance)
# v2, v3 : n 에 도착전에 거쳐야 하는 점
#
# 상황
#   1 에서 시작해서 n 에 도착한다.
#   도착하기 전에 v2, v3 을 한 번은 거쳐야 한다.
#
# 주의사항
#   1 -> n -> v2 -> v3 -> n 도 된다.
#
# 풀이
#   1 -> v2 -> v3 -> n 일때의 최단경로와
#   1 -> v3 -> v2 -> n 일때의 최단경로를 비교하면 된다.
#   각각의 최단경로는 다익스트라로 구한다.

from queue import PriorityQueue
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
connections = [[] for i in range(n + 1)]

for ee in range(e):
  a, b, c = map(int, input().split())
  connections[a].append([b, c])
  connections[b].append([a, c])

v2, v3 = map(int, input().split())

# start 에서 출발하여 end 에 도착하는 최단거리를 구한다.
def getLenTwoPoints(start, end):
  global n
  distances = [10 ** 9 for i in range(n + 1)]
  distances[start] = 0
  
  nextVisit = PriorityQueue()
  for connection in connections[start]:
    end0, dist = connection
    nextVisit.put([dist, end0])
      
  while nextVisit.qsize() > 0:
    distance, now = nextVisit.get()
    
    if distances[now] != 10 ** 9:
      continue
    
    for connection in connections[now]:
      end0, dist = connection
      if distances[end0] == 10 ** 9:
        nextVisit.put([distance + dist, end0])
    distances[now] = distance
    
  return distances[end]

# 1 -> a -> b -> n 로 가는 최단경로를 구한다.
def getLen(a, b, n):
  # 1 -> a 경로
  distance_1_to_a = getLenTwoPoints(1, a)
  # a -> b 경로
  distance_a_to_b = getLenTwoPoints(a, b)
  # b -> n 경로를 구한다.
  distance_b_to_n = getLenTwoPoints(b, n)
  
  result = distance_1_to_a + distance_a_to_b + distance_b_to_n
  return result

distance_123n = getLen(v2, v3, n)
distance_132n = getLen(v3, v2, n)

if 10 ** 9 <= distance_123n or 10 ** 9 <= distance_132n:
  print(-1)
elif 10 ** 9 <= distance_123n:
  print(distance_132n)
elif 10 ** 9 <= distance_132n:
  print(distance_123n)
else:
  print(min(distance_123n, distance_132n))
