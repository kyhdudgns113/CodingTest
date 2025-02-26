#
# N : 트리의 원소의 갯수 (N <= 1,000,000)
#
# inp[] : (U, V) 로 이루어진 배열. U번째 원소와 V번째 원소가 연결되었다는 의미
#
# 상황
#   트리의 원소는 둘 중 하나여야 한다.
#     - 자기 자신이 1 이다.
#     - 자기 자신과 직접 연결된 모든 원소가 1이다.
#
# 구하는것
#   트리 원소들의 총 합중 가장 작은값
#
# 풀이
#   루트노드를 설정한다.
#   다음 2개의 재귀함수로 풀 수 있다.
#     includeMe(now, parent)
#       - parent 는 now 의 부모노드이다.
#       - now 노드가 루트노드인 트리에서 now 가 1일때의 최소값을 리턴한다.
#       - now 의 자식노드는 0일수도, 1일수도 있다.
#         - 자식이 0인경우는 excludeMe(child, now) 를 호출
#         - 자식이 1인 경우는 includeMe(child, now) 를 호출한다.
#     excludeMe(now, parent)
#       - now 노드가 루트노드인 트리에서 now 가 0일때의 최소값을 리턴한다.
#       - now 의 자식노드는 1이어야만 한다.
#
# 주의사항
#   중복해서 계산하는 경우가 있으며, 이는 시간초과의 원인이 된다.
#   includeMe[now] 와 excludeMe[now] 를 계산하면 저장한다.
#   이후 또 호출되면 또 계산하지 않고 저장된 값을 리턴한다.
#
# 연산량
#   최악의 경우 : 트리가 1자인 경우 (모든 원소가 자식을 1개씩 가지고 있는 경우)
#   그 때마다 더하기, 메모리참조등의 연산이 발생한다
#   = O(N)
#

import sys

sys.setrecursionlimit(2000000)

input = sys.stdin.readline

N = int(input())

connections = [[] for i in range(N + 1)]
incThis = [-1 for i in range(N + 1)]
excThis = [-1 for i in range(N + 1)]

for nn in range(N - 1):
  U, V = map(int, input().split())
  connections[U].append(V)
  connections[V].append(U)
  
def includeNow(now, parent):
  
  if incThis[now] != -1:
    return incThis[now]
  
  result = 1
  for child in connections[now]:
    if child != parent:
      incChild = includeNow(child, now)
      excChild = excludeNow(child, now)
      result += min(incChild, excChild)
  
  incThis[now] = result
  return result

def excludeNow(now, parent):
  
  if excThis[now] != -1:
    return excThis[now]
  
  result = 0
  for child in connections[now]:
    if child != parent:
      result += includeNow(child, now)
      
  excThis[now] = result
  return result

print(min(includeNow(1, 1), excludeNow(1, 1)))