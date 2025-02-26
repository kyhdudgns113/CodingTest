#
# N : 트리의 원소 갯수
# R : 트리의 루트 노드의 번호
# Q : 쿼리의 갯수
# inp[] : (U, V) 로 구성된 간선의 배열 (N - 1 개)
# query[] : 쿼리의 배열. 각 쿼리는 하나의 정수로 구성 되어있다.
#
# 상황
#   주어진 입력은 항상 트리를 구성한다.
#
# 구하는것
#   각 쿼리에 해당하는 노드가 루트노드일 때
#   해당 트리의 원소의 갯수를 구한다.
#
# 풀이
#   시작 노드를 기준으로 BFS 를 이용하여 트리를 구성한다.
#   트리를 재귀함수로 구하고, 각 노드의 자손의 갯수 + 1 (본인을 포함)을 저장한다.
#   각 쿼리마다 저장된 값을 출력한다.
#
# 연산량
#   1. 트리 구성 : O(N)
#     - 모든 간선을 두 번씩만 탐색한다.
#   2. 출력 : O(Q)
#     - 쿼리마다 저장된 값을 바로 출력한다.
#

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
output = sys.stdout.write

N, R, Q = map(int, input().split())

connections = [[] for i in range(N + 1)]

for nn in range(N - 1):
  U, V = map(int, input().split())
  connections[U].append(V)
  connections[V].append(U)
  
numChilds = [0 for i in range(N + 1)]

def getChildsAndMe(now, parent):
  
  result = 1
  for child in connections[now]:
    if numChilds[child] == 0 and child != parent:
      result += getChildsAndMe(child, now)
      
  numChilds[now] = result
  return numChilds[now]

getChildsAndMe(R, R)

for query in range(Q):
  U = int(input())
  output("%d\n" % numChilds[U])