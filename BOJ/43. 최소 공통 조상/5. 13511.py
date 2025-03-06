# pypy 로 돌려야 한다.
#
# N : 트리의 노드 개수 (N <= 100,000)
# inp[] : (U, V, W) 로 구성된 N - 1 개의 배열.
#           U 랑 V 가 길이 W 로 연결되었음을 뜻한다.
# M : 쿼리의 갯수 (M <= 100,000)
# query[] : 다음 두 경우중 하나이다.
#           1 U V : U 에서 V 로 갈 때 거리를 구한다.
#           2 U V K : U 에서 V 로 갈 때, K 번째 원소를 구한다.
#
# 상황
#   트리 구조가 들어온다.
#
# 풀이
#   다음 배열들을 이용하면 각 탐색마다 N 이 아닌 log N 으로 구할 수 있다.
#     Pki[k][i] : i 번째 노드의 2^k 번째 조상
#     sumPki[k][i] : i 번째 노드와 2^k 번째 조상 사이의 거리
#     두 배열을 완성하는 시간은
#       k 의 크기 : log N
#       i 의 크리 : N
#       = O(N log N) 에 완성할 수 있다.
#
#   함수 1. node 의 depth 번째 조상 찾기 : O(log N)
#     Pki 배열을 이용하여 찾는다.
#     depth 를 이진수로 봤을때 해당 비트의 k 만큼 이동한다.
#       depth = 5 = 0x1011 이라 했을때
#         1번째 비트가 1 이므로 
#           - node = Pki[1][node]
#           - 경로합 += sumPki[1][node]
#         2번째 비트는 0 이므로 무시
#         3번째 비트는 1 이므로 
#           - node = Pki[3][node]
#           - 경로합 += sumPki[3][node]
#         4번째 비트는 1 이므로 
#           - node = Pki[4][node]
#           - 경로합 += sumPki[4][node]
#
#   함수 2. 최소 공통 조상 찾기 : O(log N * log N)
#     일단 두 노드의 깊이를 동일하게 만든다.
#       더 깊은 노드를 Pki 를 이용하여 같은 깊이로 맞춰준다.
#       Pki 로 이동할때 sumPki 도 사용하여 경로 합을 구한다.
#         
#     (0, 현재 depth) 범위에서 이진탐색으로 최소 공통조상을 찾는다.
#       Pki 배열을 이용하면 각 탐색마다 logN 으로 수행 가능하다.
#         경로합 += sumPki[k][Node] (이걸 꼭 먼저 해야 한다.)
#         Node = Pki[k][Node]
#
#   쿼리 1. 두 노드 U, V 사이의 거리 구하기
#     1. 두 노드의 깊이를 맞추고, 그 과정에서의 경로합을 구한다.
#     2. 두 노드의 최소 공통 조상을 찾고, 그 과정에서 경로합을 구한다.
#
#   쿼리 2. U 에서 V 로 갈 때 K 번째 노드 찾기
#     1, 2 는 동일. 단, 최소 공통조상까지 depth 차이도 구한다.
#     3. K 가 U 에서 최소 공통조상을 넘지는 못하는 경우
#       - U 의 K 번째 조상을 리턴한다.
#     4. K 가 U 의 최소 공통조상을 넘어가는 경우
#       - V 의 X 번째 조상을 리턴한다.
#         X = A - (K - B)
#         A : 조상에서 V 까지의 깊이 차이
#         B : 조상에서 U 까지의 깊이 차이
#
# 연산량
#   배열완성 : O(N log N)
#   각 쿼리마다 최소 공통 조상 찾기 : O(M * log N * log N)
#   = 약 수천만
#   = pypy 로 돌려야 한다.


import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
connections = [[] for i in range(N + 1)]

for nn in range(N - 1):
  U, V, W = map(int, input().split())
  connections[U].append((V, W))
  connections[V].append((U, W))
  
parentArr = [i for i in range(N + 1)]
distParentArr = [0 for i in range(N + 1)]
depthArr = [0 for i in range(N + 1)]

#
# 트리 만드는 부분
#
def makeTree(now, parent, depth, dist):
  parentArr[now] = parent
  distParentArr[now] = dist
  depthArr[now] = depth
  
  for child, dist0 in connections[now]:
    if child != parent:
      makeTree(child, now, depth + 1, dist0)

makeTree(1, 1, 0, 0)

#
# Pki 배열 만드는 부분
#
Pki = [[0 for i in range(N + 1)] for k in range(19)]
sumPki = [[0 for i in range(N + 1)] for k in range(19)]

for i in range(1, N + 1):
  Pki[1][i] = parentArr[i]
  sumPki[1][i] = distParentArr[i]
for k in range(2, 19):
  for i in range(1, N + 1):
    Pki[k][i] = Pki[k - 1][Pki[k - 1][i]]
    sumPki[k][i] = sumPki[k - 1][i] + sumPki[k - 1][Pki[k - 1][i]]
    
#
# 1 번 함수
# node 의 depth 번째 조상을 구한다.
# 리턴값 : (조상, 조상까지의 거리)
#
def findAncesstor(node, depth):
  k = 1
  sumLength = 0
  while depth > 0:
    if depth % 2 == 1:
      sumLength += sumPki[k][node]
      node = Pki[k][node]
    k += 1
    depth //= 2
  return (node, sumLength)

#
# 2 번 함수수
# Node1 과 Node2 의 최소 공통 조상을 구한다.
#   리턴값 : (공통조상, 공통조상과의 깊이차이, 경로 길이 합)
#
def LCA(Node1, Node2, depth):
  minDepth = 0
  maxDepth = depth
  
  while minDepth + 1 <= maxDepth:
    centerDepth = (minDepth + maxDepth) // 2
    next1, _ = findAncesstor(Node1, centerDepth)
    next2, _ = findAncesstor(Node2, centerDepth)
    
    if next1 == next2:
      maxDepth = centerDepth
    else:
      minDepth = centerDepth + 1
      
  next1, sum1 = findAncesstor(Node1, minDepth)
  next2, sum2 = findAncesstor(Node2, maxDepth)
  
  if next1 == next2:
    return (next1, minDepth, sum1 + sum2)
  else:
    next1, sum1 = findAncesstor(Node1, maxDepth)
    next2, sum2 = findAncesstor(Node2, maxDepth)
    return (next1, maxDepth, sum1 + sum2)

#
# 1 번 쿼리를 실행하는곳
# U 와 V 사이의 거리를 구한다.
#
def getPathLength(U, V):
  Node1, Node2, depth1, depth2 = (U, V, depthArr[U], depthArr[V])
  if depth1 < depth2:
    Node1, Node2, depth1, depth2 = (V, U, depth2, depth1)
  
  sumLength = 0  
  delta = depth1 - depth2
  k = 1
  while delta > 0:
    if delta % 2 == 1:
      sumLength += sumPki[k][Node1]
      Node1 = Pki[k][Node1]
    k += 1
    delta //= 2
    
  lca, depth, retLength = LCA(Node1, Node2, depth2)
  return sumLength + retLength

#
# 2 번 쿼리를 실행하는곳
# U 에서 V 를 향해 K 번째에 있는 원소를 구한다.
#   1번째는 U 이다.
#
def getNextNode(U, V, K):
  # K = 1 이면 이동을 하면 안된다.
  K -= 1
  
  # 두 노드의 깊이를 맞춰준다.
  # Pki 배열을 이용하여 log 시간에 수행한다.
  # 더 깊은 노드를 Node1 로 설정한다.
  #   diffDepth : Node1, Node2 의 깊이 차이의 절대값값
  Node1, Node2, depth1, depth2 = (U, V, depthArr[U], depthArr[V])
  isUDeeper = True
  diffDepth = depth1 - depth2
  
  if depth1 < depth2:
    diffDepth = depth2 - depth1
    Node1, Node2, depth1, depth2 = (V, U, depth2, depth1)
    isUDeeper = False
    
  sumLength = 0  
  delta = depth1 - depth2
  k = 1
  while delta > 0:
    if delta % 2 == 1:
      sumLength += sumPki[k][Node1]
      Node1 = Pki[k][Node1]
    k += 1
    delta //= 2
    
  lca, depth, retLength = LCA(Node1, Node2, depth2)
  
  # K 번째 노드가 공통조상을 넘어가진 않은 경우우
  if K <= depth + (diffDepth if isUDeeper else 0):
    result, _ = findAncesstor(U, K)
    return result
  # K 번째 노드가 공통조상을 넘어간 경우
  else:
    result, _ = findAncesstor(V, depth + diffDepth - K + depth)
    return result    

#
# 쿼리 실행하는 부분
#
M = int(input())

for mm in range(M):
  query = list(map(int, input().split()))
  
  if query[0] == 1:
    U, V = query[1::]
    output("%d\n" % getPathLength(U, V))
  else:
    U, V, K = query[1::]
    output("%d\n" % getNextNode(U, V, K))
