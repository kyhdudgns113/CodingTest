#
# pypy 로 돌려야 한다.
#
# N : 트리의 원소의 갯수 (N <= 100,000)
# input[] : (A, B) 로 이루어진 N - 1 개의 배열. A 와 B 가 연결되었다는 의미
# M : 쿼리의 갯수 (M <= 100,000)
# query[] : (A, B) 로 이루어진 M 개의 배열.
#
# 상황
#   1 부터 N 까지의 원소로 트리가 구성되어 있다.
#   루트노드는 1이다.
#
# 구하는것
#   각 쿼리 (A, B) 마다
#     A 와 B 의 최소 공통 조상을 구한다.
#
# 풀이
#   기본 아이디어는 43 -> 1 -> 3585.py 랑 같다.
#   공통 조상을 찾을때 이진탐색으로 찾을 수 있게 한다.
#     아래 배열을 완성한다.
#       Pki[k][i] : i 의 2^k 번째 조상노드
#   1. 두 노드의 깊이를 같게 만든다.
#     더 깊은 노드의 부모노드를 Pki 를 이용하여 갱신한다.
#       이러면 깊이차이가 depth 일때 log depth 만큼만 연산해도 된다.
#   2. 바뀐 두 노드의 최소 공통조상을 Pki 배열을 이용하여 이진탐색으로 찾는다.
#
# 연산량
#   1. Pki 배열 완성
#     모든 노드 N 개에 대하여
#     log 최대깊이 만큼 연산한다.
#     = O(N) * O(log N)
#     = O(N log N)
#   2. 각 쿼리마다 : O(M)
#     - 두 노드의 깊이를 맞춘다 : O(log N)
#     - 두 노드의 공통 조상을 찾는다 : O(log N * log N)
#       - 모든 깊이마다 : O (log N)
#       - 깊이만큼의 조상을 찾는다 : O(log N)
#   1 + 2 = O(N log N + M log N * log N)
#   = 약 수백~수천만
#
#   python3 으로 돌리면 시간초과가 나고, pypy 로 돌려야 한다.
#

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

# 입력 : 트리의 간선을 입력받는다.
connections = [[] for i in range(N + 1)]
for nn in range(N - 1):
  A, B = map(int, input().split())
  connections[A].append(B)
  connections[B].append(A)

# parentArr[i] : i 의 부모노드
# depthArr[i] : i 의 트리 깊이
# Pki[k][i] : i 의 2^k 번째 조상상
parentArr = [i for i in range(N + 1)]
depthArr = [0 for i in range(N + 1)]
Pki = [[0 for i in range(N + 1)] for k in range(19)]

# parent 를 부모로 갖고
# 깊이가 depth 인 now 를 기준으로 트리를 완성한다.
def makeTree(now, parent, depth):
  parentArr[now] = parent
  depthArr[now] = depth
  
  for child in connections[now]:
    if child != parent:
      makeTree(child, now, depth + 1)

# node 의 depth 번째 조상을 구한다.
# 연산량은 O(log depth) 이다.
def findAncesstor(node, depth):
  k = 1
  while depth > 0:
    if depth % 2 == 1:
      node = Pki[k][node]
    k += 1
    depth //= 2
  return node

# Node1 과 Node2 의 최소 공통 조상을 구한다.
# 이들의 현재 깊이는 depth 이다.
# 이진탐색으로 최소 공통조상의 depth 를 구한다.
def LCA(Node1, Node2, depth):
  minDepth = 0
  maxDepth = depth
  
  while maxDepth - minDepth > 1:
    centerDepth = (maxDepth + minDepth) // 2
    anc1 = findAncesstor(Node1, centerDepth)
    anc2 = findAncesstor(Node2, centerDepth)
    
    if anc1 == anc2:
      maxDepth = centerDepth
    else:
      minDepth = centerDepth + 1
  
  anc1 = findAncesstor(Node1, minDepth)
  anc2 = findAncesstor(Node2, minDepth)
  
  if anc1 == anc2:
    return anc1
  else:
    return findAncesstor(Node1, maxDepth)
  
# 트리를 만든다.
makeTree(1, 1, 0)

# Pki 배열을 완성한다
for i in range(1, N + 1):
  Pki[1][i] = parentArr[i]
  
for k in range(2, 19):
  for i in range(1, N + 1):
    Pki[k][i] = Pki[k - 1][Pki[k - 1][i]]
      
# 쿼리를 실행한다.
M = int(input())
for query in range(M):
  A, B = map(int, input().split())
  
  # A, B 둘 중 깊이가 더 깊은 노드를 Node1 으로 한다.
  Node1, Node2, depth1, depth2 = (A, B, depthArr[A], depthArr[B])
  if depthArr[A] <= depthArr[B]:
    Node1, Node2, depth1, depth2 = (B, A, depthArr[B], depthArr[A])
  
  # Node1, Node2 의 깊이를 같도록 만든다.
  K = depth1 - depth2
  k = 1
  while K > 0:
    if K % 2 == 1:
      Node1 = Pki[k][Node1]
    k += 1
    K //= 2
  
  # Node1, Node2 의 LCA 를 구하고 출력한다.
  output("%d\n" % LCA(Node1, Node2, depth1))