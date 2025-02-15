#
# v : 점의 갯수
# e : 간선의 갯수
# 추가입력 : (시작점, 끝점, 거리) 로 구성된 e 개의 배열
#
# 구하는것
#   시작점과 끝점이 동일한 경로중 최단거리
#     없으면 -1
#
# 풀이
#   플로이드-와샬 알고리즘을 구현하면 된다.
#   최단거리가 INF 면 -1을 출력하게 하면 된다.

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
distances = [[10 ** 9 for i in range(v + 1)] for j in range(v + 1)]

for ee in range(e):
  start, end, dist = map(int, input().split())
  distances[start][end] = dist
  
for mid in range(1, v + 1):
  for start in range(1, v + 1):
    for end in range(1, v + 1):
      distances[start][end] = min(
        distances[start][end],
        distances[start][mid] + distances[mid][end]
      )
      
result = 10 ** 9
for i in range(1, v + 1):
  result = min(result, distances[i][i])
  
if result == 10 ** 9:
  print(-1)
else:
  print(result)