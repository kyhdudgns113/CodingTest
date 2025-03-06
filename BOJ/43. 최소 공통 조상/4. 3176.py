#
# pypy 로 돌려야 한다.
#
# N : 트리 구조로 된 도시의 개수
# inp[] : (A, B, C) 로 이루어진 N - 1 개의 배열. A 와 B 사이의 거리가 C 라는 뜻
# M : 쿼리의 수
# query[] : (D, E) 로 이루어진 M 개의 쿼리 배열
#
# 상황
#   도시들은 트리 구조를 이룬다.
#
# 구하는것
#   D 와 E 사이에 있는 도로중 가장 짧은것과 가장 긴 것을 출력한다.
#
# 풀이
#   다음 배열들을 만들어 문제를 풀 수 있다.
#     Pki[k][i] : 도시 i 의 2^k 번째 부모도시
#     minPki[k][i] : 도시 i 와 2^k 번째 부모도시 사이에 있는 도로중 가장 짧은것
#     maxPki[k][i] : 도시 i 와 2^k 번째 부모도시 사이에 있는 도로중 가장 긴 것
#
#   1. 트리구조를 만든다.
#     - 해당 노드의 깊이, 부모노드, 부모노드와의 거리를 저장한다.
#   2. 위 배열들을 만든다.
#   
#   각 쿼리의 입력 D, E 마다
#     3. 둘 중 더 깊은 노드를 더 얕은 노드와 깊이가 같게 한다.
#       - 깊이를 1씩 낮추지 않고, Pki 배열을 이용하여 log 시간에 수행한다.
#       - 이 과정에서 더 깊은 노드가 위로 이동하면서 가장 짧은 도로와 가장 긴 도로를 갱신한다.
#     4. 두 노드의 최소 공통 조상(LCA)을 찾는다.
#       - 이 과정도 Pki 배열을 활용한다.
#       - 공통 조상으로 거슬러 올라가면서 최소값, 최대값을 갱신한다.
#
# 연산량
#   1. 트리구조 만들기 : O(N)
#   2. Pki 배열 만들기 : O(N log N)
#   3. 각 쿼리마다 * 노드 깊이 일치시키기 : O(M) * O(log N)
#   4. 각 쿼리마다 LCA 찾기 : O(M) * O(logN * logN)
#       LCA 를 찾을때 연산이 O(logN * logN) 이다.
#         - 공통조상의 depth 를 이진탐색으로 찾는 연산 : O(log N)
#         - 해당 depth 번째 조상의 번호를 확인하는 연산 : O(log N)
#
#   1 + 2 + 3 + 4 = O(N log N + M logN*logN)
#   = 약 4천만
#   = pypy 로 돌려야 한다.
#

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

connections = [[] for i in range(N + 1)]

for nn in range(N - 1):
  A, B, C = map(int, input().split())
  connections[A].append((B, C))
  connections[B].append((A, C))
  
parentArr = [[i, 0] for i in range(N + 1)]
depthArr = [0 for i in range(N + 1)]

# 1. 트리 구조를 만든다.
def makeTree(now, parent, depth, distance):
  parentArr[now] = [parent, distance]
  depthArr[now] = depth
  
  for child, dist0 in connections[now]:
    if child != parent:
      makeTree(child, now, depth + 1, dist0)
      
makeTree(1, 1, 0, 0)

#
# 2. Pki 배열들을 완성한다.
#
Pki = [[0 for i in range(N + 1)] for j in range(19)]
minPki = [[-1 for i in range(N + 1)] for j in range(19)]
maxPki = [[-1 for i in range(N + 1)] for j in range(19)]

for i in range(1, N + 1):
  parent, dist = parentArr[i]
  Pki[1][i] = parent
  minPki[1][i] = dist
  maxPki[1][i] = dist
  
for k in range(2, 19):
  for i in range(1, N + 1):
    Pki[k][i] = Pki[k - 1][Pki[k - 1][i]]
    minPki[k][i] = min(
      minPki[k - 1][i],
      minPki[k - 1][Pki[k - 1][i]]
    )
    maxPki[k][i] = max(
      maxPki[k - 1][i],
      maxPki[k - 1][Pki[k - 1][i]]
    )

def findAncesstor(Node1, depth):
  k = 1
  minVal = 10 ** 9
  maxVal = 0
  while depth > 0:
    if depth % 2 == 1:
      minVal = min(minVal, minPki[k][Node1])
      maxVal = max(maxVal, maxPki[k][Node1])
      Node1 = Pki[k][Node1]
    depth //= 2
    k += 1
  return (Node1, minVal, maxVal)

def LCA(Node1, Node2, depth):
  minDepth = 0
  maxDepth = depth
  
  while minDepth + 1 <= maxDepth:
    centerDepth = (minDepth + maxDepth) // 2
    next1, min1, max1 = findAncesstor(Node1, centerDepth)
    next2, min2, max2 = findAncesstor(Node2, centerDepth)
    if next1 == next2:
      maxDepth = centerDepth
    else:
      minDepth = centerDepth + 1
  next1, min1, max1 = findAncesstor(Node1, minDepth)
  next2, min2, max2 = findAncesstor(Node2, minDepth)
  
  if next1 == next2:
    return (next1, min(min1, min2), max(max1, max2))
  else:
    next1, min1, max1 = findAncesstor(Node1, maxDepth)
    next2, min2, max2 = findAncesstor(Node2, maxDepth)
    return (next1, min(min1, min2), max(max1, max2))

def getMinMax(D, E):
  Node1, Node2, depth1, depth2 = (D, E, depthArr[D], depthArr[E])
  
  if depth1 < depth2:
    Node1, Node2, depth1, depth2 = (E, D, depthArr[E], depthArr[D])
  
  # 3. 둘 중 더 깊은 노드를 얕은 노드의 깊이에 맞춘다.
  #     - Pki 배열을 이용한다.
  #     - 이 과정에서 minVal, maxVal 을 갱신한다.
  minVal = 10 ** 9
  maxVal = 0
  K = depth1 - depth2
  k = 1
  while K > 0:
    if K % 2 == 1:
      minVal = min(minVal, minPki[k][Node1])
      maxVal = max(maxVal, maxPki[k][Node1])
      Node1 = Pki[k][Node1]
    K //= 2
    k += 1
    
  lca, min0, max0 = LCA(Node1, Node2, depth2)
  minVal = min(minVal, min0)
  maxVal = max(maxVal, max0)
  
  return (minVal, maxVal)
#
# 쿼리를 입력받는다.
#
K = int(input())

for kk in range(K):
  D, E = map(int, input().split())

  minVal, maxVal = getMinMax(D, E)
  output("%d %d\n" % (minVal, maxVal))
