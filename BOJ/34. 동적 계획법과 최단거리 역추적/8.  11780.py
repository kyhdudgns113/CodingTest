#
# n : 점의 갯수 (n <= 1,000)
# m : 단방향 간선의 갯수 (m <= 100,000)
# inp[] : (start, end, distance) 로 구성된 길이 m 의 배열 (distance <= 100,000)
#
# 구하는것
#   1. 각 점에서 각 점까지 가는데 걸리는 최단거리 (N 줄에 대하여 N 칸씩)
#     - 갈 수 없으면 0 출력
#   2. i 번째 점에서 j 번째 점까지 최단경로 자체를 출력 (N * N 줄에 대하여 출력)
#     - 경로가 없으면 0 출력
#
# 풀이
#   플로이드-와샬 알고리즘을 사용하면 된다.
#   start 부터 end 까지의 최단거리가 (start, mid) + (mid, end) 로 갱신되면
#     - start 와 end 의 중간지점을 mid 로 설정한다.
#     - 이 후 재귀함수로 start 와 end 사이의 경로를 출력할 수 있게 한다.
#

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
m = int(input())

distances = [[[10 ** 9, -1] for i in range(n + 1)] for j in range(n + 1)]

for mm in range(m):
  a, b, c = map(int, input().split())
  if distances[a][b][0] > c:
    distances[a][b][0] = c

for i in range(1, n + 1):
  distances[i][i][0] = 0
  
for mid in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      tempSum = distances[start][mid][0] + distances[mid][end][0]
      
      if distances[start][end][0] > tempSum:
        distances[start][end] = [tempSum, mid]
        
# 최단거리 출력
for start in range(1, n + 1):
  for end in range(1, n + 1):
    dist, _ = distances[start][end]
    
    if dist == 10 ** 9:
      output("0 ")
    else:
      output("%d " % dist)
  output("\n")

# start 와 end 사이에 있는 경로들의 배열을 리턴한다.
# incStart 와 incEnd 가 True 여야만 start 와 end 를 포함하여 리턴한다.
#   처음 호출할때만 True 이다.
def getString(start, end, incStart, incEnd):
  if start == end:
    return []
  
  mid = distances[start][end][1]
  result = []
  if mid != -1 and start != mid and mid != end:
    result = getString(start, mid, False, False) + \
      [mid] + \
      getString(mid, end, False, False)
  
  if incStart == True:
    result = [start] + result
  if incEnd == True:
    result = result + [end]
    
  return result

# 경로 출력력
for start in range(1, n + 1):
  for end in range(1, n + 1):
    if distances[start][end][0] == 10 ** 9:
      output("0\n")
    else:
      result = getString(start, end, True, True)
      output("%d " % len(result))
      for num in result:
        output("%d " % num)
      output("\n")