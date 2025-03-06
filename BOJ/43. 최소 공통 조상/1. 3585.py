#
# N : 트리의 노드 수 (N <= 10,000)
# input[] : (A, B) 로 구성된 N - 1 크기의 배열. A 가 B 의 부모 노드임을 알려준다.
# Node1, Node2 : 공통 조상을 구할 두 노드
#
# 구하는것
#   Node1, Node2 의 공통 조상중 가장 가까운것을 구한다.
#
# 풀이
#   트리를 구성한다.
#   Node1, Node2 를 같은 depth 가 될때까지 각자의 부모를 향해 이동한다.
#   둘이 같아질때까지 한 단계씩 부모노드로 이동한다.
#
# 연산량
#   트리 구성하는 연산 : O(N)
#     나의 부모가 누군지, 자식이 누군지만 저장한다.
#     이는 O(N) 으로 해결이 된다.
#   같은 depth 가 될 때까지 올라가는 연산 : O(log N)
#   둘이 같아질때까지 부모로 이동하는 연산 : O(log N)
#   = O(N) + O(log N) + O(log N)
#   = O(N)
#

from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for testCase in range(T):
  N = int(input())
  parentArr = [i for i in range(N + 1)]
  childsArr = [[] for i in range(N + 1)]
  depthArr = [0 for i in range(N + 1)]
  
  for nn in range(N - 1):
    A, B = map(int, input().split())
    parentArr[B] = A
    childsArr[A].append(B)
    
  Node1, Node2 = map(int, input().split())
  
  # 트리를 구성하기 위해 루트노드를 찾는다.
  nextVisit = deque()
  for i in range(1, N + 1):
    if parentArr[i] == i:
      nextVisit.append((i, 0))
      break
    
  # 자식 노드들을 찾아서 depth 값을 설정한다.
  while len(nextVisit) > 0:
    now, depth = nextVisit.popleft()
    depthArr[now] = depth
    
    for child in childsArr[now]:
      nextVisit.append((child, depth + 1))
      
  depth1, depth2 = (depthArr[Node1], depthArr[Node2])
  
  # 두 노드중 깊이가 더 깊은 노드를 NodeA, 더 깊은 깊이를 depthA 로 한다.
  NodeA, NodeB = (Node1, Node2) if depth1 > depth2 else (Node2, Node1)
  depthA, depthB = (depth1, depth2) if depth1 > depth2 else (depth2, depth1)
  
  # 일단 깊이를 맞춰준다.
  while depthA > depthB:
    NodeA = parentArr[NodeA]
    depthA -= 1
    
  # 공통 조상을 발견할때까지 한 단계씩 부모 노드로 이동한다.
  while NodeA != NodeB:
    NodeA = parentArr[NodeA]
    NodeB = parentArr[NodeB]
    
  print(NodeA)
  