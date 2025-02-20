#
# 각 테스트 케이스에 대하여
# n : 점의 갯수 (n <= 500)
# m : 간선의 갯수 (m <= nC2)
# n, m == 0, 0 이면 입력 종료
#
# inp[] : (시작점, 도착점) 으로 이루어진 m 개의 배열. 양방향 간선임.
#
# 구하는것
#   해당 간선들로 구성한 그래프에서 트리의 갯수
#
# 풀이
#   bfs 로 풀 수 있다.
#     시작점의 부모노드는 자기 자신(now)으로 설정한다.
#     now랑 연결된 노드중에서
#       now 의 부모노드가 아닌데 부모노드가 설정된 노드가 있으면 그곳은 루프가 존재한다.
#         최종적으로 1을 리턴하게 한다.
#       now 의 자식 노드중에서 재귀함수로 1을 리턴하는 경우가 있을때
#         최종적으로 1을 리턴하게 한다.
#       둘 다 아니면 0을 리턴한다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

def findLoop(connections, parentArr, now):
  
  parent = parentArr[now]
  result = 0
  for next in connections[now]:
    if parentArr[next] != -1 and next != parent:
      result = 1
    elif next != parent:
      parentArr[next] = now
      if findLoop(connections, parentArr, next) == 1:
        result = 1
  
  return result

caseNum = 1

while True:
  n, m = map(int, input().split())
  
  if n == 0 and m == 0:
    break
  
  connections = [[] for i in range(n + 1)]
  
  for mm in range(m):
    start, end = map(int, input().split())
    connections[start].append(end)
    connections[end].append(start)
  
  parentArr = [-1 for i in range(n + 1)]
  
  numTrees = 0
  for i in range(1, n + 1):
    # i 번째 점을 방문한적이 없을때 bfs 를 돌린다.
    if parentArr[i] == -1:
      parentArr[i] = i
      
      # 일단 트리 갯수를 1 늘린다.
      numTrees += 1
      
      # 루프가 존재하면 트리 개수를 1 뺀다.
      numTrees -= findLoop(connections, parentArr, i)
  
  if numTrees == 0:
    output("Case %d: No trees.\n" % caseNum)
  elif numTrees == 1:
    output("Case %d: There is one tree.\n" % caseNum)
  else:
    output("Case %d: A forest of %d trees.\n" % (caseNum, numTrees))
  caseNum += 1
      