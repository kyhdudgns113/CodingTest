# n : 도시의 갯수 (n <= 100)
# m : 두 도시를 잇는 간선의 갯수 (m <= 100,000)
# 간선정보 : (start, end, dist) 시작, 끝, 거리 로 구성된 간선정보의 배열
#
# 상황
#   start, end 가 중복된 간선이 있을 수 있다.
#   음수인 간선은 없다.
#
# 구하는것
#   모든 도시에서 모든 도시로 가는 최단거리의 배열
#     갈 수 없으면 0 출력
#
# 풀이
#   플로이드-와샬 알고리즘으로 풀면 된다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
m = int(input())
  
distances = [[10 ** 9 for i in range(n + 1)] for j in range(n + 1)]

for mm in range(m):
  start, end, dist = map(int, input().split())
  distances[start][end] = min(distances[start][end], dist)

for i in range(n + 1):
  distances[i][i] = 0
  
for mid in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      distances[start][end] = min(
        distances[start][end],
        distances[start][mid] + distances[mid][end]
      )

for i in range(1, n + 1):
  for j in range(1, n + 1):
    val = distances[i][j]
    if val == 10 ** 9:
      output("0 ")
    else:
      output("%d " % (val))
  output("\n")