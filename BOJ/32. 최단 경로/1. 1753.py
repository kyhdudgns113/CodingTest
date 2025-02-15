#
# v : 점의 개수
# e : 간선의 개수
# k : 시작점의 번호
# connections[i] : i 번째 점에서 시작하는 간선의 배열 (end, distance)
#
# 구하는것
#   k 번째 점에서 나머지 점까지의 최단거리 전부
#
# 풀이
#   다익스트라 알고리즘을 구현하면 된다.

from queue import PriorityQueue
import sys

input = sys.stdin.readline
output = sys.stdout.write

v, e = map(int, input().split())
k = int(input())
connections = [[] for i in range(v + 1)]

for ee in range(e):
  start, end, distance = map(int, input().split())
  connections[start].append([end, distance])
  
nextEdges = PriorityQueue()
distances = [10 ** 9 for i in range(v + 1)]
distances[k] = 0

for connection in connections[k]:
  end, distance = connection
  distances[end] = distance
  nextEdges.put([distance, k, end])

isVisit = [0 for i in range(v + 1)]
isVisit[k] = 1

while nextEdges.qsize() > 0:
  distance, _, start = nextEdges.get()
  if isVisit[start] != 0:
    continue
  distances[start] = distance
  
  for connection in connections[start]:
    end, dist0 = connection
    if isVisit[end] == 0:
      nextEdges.put([distance + dist0, start, end])
  
  isVisit[start] = 1

for i in range(1, v + 1):
  distance = distances[i]
  if distance == 10 ** 9:
    output("INF\n")
  else:
    output("%d\n" % (distance))
  
  