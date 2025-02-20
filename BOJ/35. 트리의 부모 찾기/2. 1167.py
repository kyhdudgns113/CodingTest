#
# n : 점의 숫자
# inp[i] : i 번째 점과 연결된 모든 점들의 (목적지, 거리) 의 배열. 일렬로 옴. -1로 끝남
#
# 상황
#   트리 구조를 이룬다.
#
# 구하는것
#   가장 먼 두 점 사이의 거리
#
# 풀이
#   트리 구조로 되어있으면 어느 한 점을 루트 노드로 설정해도 무방하다.
#     - 1을 루트 노드로 설정한다.
#   1과 연결된 노드들부터 각 노드들의 부모노드를 설정한다.
#     - bfs 로 구할 수 있다.
#   루트 노드부터 다음을 구한다.
#     getResult(now) : now 와 children 의 연결중에서 거리가 가장 먼 것을 리턴
#       1. now 의 각 children 에 대하여
#         - getResult(children) + distance[now][children] 을 배열에 넣는다.
#       2. 배열의 크기가 2보다 크면
#         - 가장 큰 두 값이랑 구하고자 하는 최대값이랑 비교하고 큰 값으로 대체
#       3. 배열의 크기가 1이면
#         - 해당 값이랑 구하고자 하는 최대값이랑 비교후 갱신
#       4. 배열의 크기가 0이면
#         - 아무것도 하지 않음
#       이후 배열에 있는 수 중에서 가장 큰 수를 리턴
#
# 
#

from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

connections = [[] for i in range(n + 1)]

# 각 점과 연결되어 있는 간선들을 입력받는 부분
for i in range(n):
  inp = list(map(int, input().split()))
  start = inp[0]
  idx = 1
  
  while idx < len(inp) - 1:
    a, b = inp[idx], inp[idx + 1]
    connections[start].append([b, a])
    idx += 2
    
parentNumber = [[-1, -1] for i in range(n + 1)]
parentNumber[1] = [0, 1]

nextVisit = deque()
nextVisit.append(1)

# 점 1에서 시작하여 각 노드들의 부모노드와 거리를 구하는 부분
while len(nextVisit) > 0:
  now = nextVisit.popleft()
  
  for connection in connections[now]:
    dist, next = connection
    if parentNumber[next][0] == -1:
      parentNumber[next] = [dist, now]
      nextVisit.append(next)

globalResult = 0

# now 의 자식들 중에서 최대 거리를 구한다.
def getResult(now):
  global globalResult
  
  nowParent = parentNumber[now][1]
  resultArr = []
  
  # 자식 노드들에 대하여 거리들을 배열에 넣는다.
  for connection in connections[now]:
    dist, children = connection
    if children != nowParent:
      resultArr.append(getResult(children) + dist)
  resultArr.sort()
  resultArr.reverse()
  
  lenResult = len(resultArr)
  result = 0
  if lenResult == 0:
    result = 0
  elif lenResult == 1:
    result = resultArr[0]
  else:
    result = resultArr[0] + resultArr[1]
  globalResult = max(globalResult, result)
  return resultArr[0] if lenResult > 0 else 0

getResult(1)
print(globalResult)
  
