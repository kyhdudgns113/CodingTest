# k : 테스트 케이스 개수
# v : 점의 개수
# e : 간선의 갯수
# conn[] : (start, end) 로 이루어진 간선의 연결
#
# 상황
#   점의 집합을 둘로 분리하여 같은 집합에 속한 점은 서로 연결되어있지 않게 한다.
#
# 구하는것
#   이게 가능하면 "YES", 아니면 "NO" 를 출력한다.
#
# 풀이
#   bfs 로 풀면 쉽다.
#     현재 점이 속한 그룹을 1 이라 하자.
#     이 점이랑 연결된 점들은 그룹 2 에 속해야 한다.
#     만약 연결된 점들중 그룹 1 에 속해있는 점이 하나라도 존재하면 NO 를 출력
#     에러가 없다면 해당 점들이 그룹 2에 속하도록 하고 bfs 큐에 넣는다.
#
# 유의할 점
#   1번째 점에서 bfs 를 시작한다고 했을떄, 1과 연결되지 않은 점들이 있을 수 있다.
#   모든 점들에 대해 순환하는 반복문을 하나 더 씌워줌으로써 해결한다.
#     방문한적 없는 점에 대해서만 bfs 를 추가로 돌도록 한다.

from collections import deque
import sys

input = sys.stdin.readline

k = int(input())

for kk in range(k):
  v, e = map(int, input().split())
  conn = [[] for i in range(v + 1)]
  
  for ee in range(e):
    start, end = map(int, input().split())
    conn[start].append(end)
    conn[end].append(start)
    
  isVisit = [0 for i in range(v + 1)]
  nextVisit = deque()
  result = "YES"
  
  for now in range(1, v + 1):
    if isVisit[now] == 0:
      isVisit[now] = 1
      nextVisit.append(now)
      
      groupNumber = 1
      while len(nextVisit) > 0:
        start = nextVisit.popleft()
        nextGroup = (isVisit[start] % 2) + 1
        
        for end in conn[start]:
          if isVisit[end] == isVisit[start]:
            result = "NO"
          elif isVisit[end] == 0:
            isVisit[end] = nextGroup
            nextVisit.append(end)
  print(result)