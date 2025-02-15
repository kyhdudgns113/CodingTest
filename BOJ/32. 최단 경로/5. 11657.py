#
# n : 도시의 갯수
# m : 두 도시를 잇는 도로의 갯수
# connections[] : (start, end, dist) 시작점, 끝점, 거리의 배열
#
# 상황
#   도시 1 에서 출발하여 다른 도시로 가는 최단거리를 구하려 한다.
#   거리느 음수일 수 있다.
#
# 구하는것
#   만약 무한한 음수로 내려가는 경우가 있으면 -1 만 출력
#   아니면 2번 도시부터 n번 도시까지 거리를 출력
#     도착 못하면 -1 출력
#
# 풀이
#   벨만포드 알고리즘을 구현하면 된다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())
connections = [[] for i in range(n + 1)]

for mm in range(m):
  a, b, c = map(int, input().split())
  connections[a].append([b, c])
  
distances = [10 ** 9 for i in range(n + 1)]
distances[1] = 0

for _ in range(n):
  for start in range(1, n + 1):
    if distances[start] == 10 ** 9:
      continue
    for conn in connections[start]:
      next, dist = conn
      distances[next] = min(distances[next], distances[start] + dist)
      
isInfinity = 0

for _ in range(n - 1):
  for start in range(1, n + 1):
    if distances[start] == 10 ** 9:
      continue
    for conn in connections[start]:
      next, dist = conn
      if distances[next] > distances[start] + dist:
        distances[next] = distances[start] + dist
        isInfinity = 1
        
if isInfinity == 1:
  print(-1)
else:
  for dest in range(2, n + 1):
    if distances[dest] == 10 ** 9:
      output("-1\n")
    else:
      output("%d\n" % (distances[dest]))
      