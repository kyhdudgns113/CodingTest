#
# N : 트리의 원소의 갯수 (N <= 10,000)
# WArr[] : 원소마다 가중치의 배열 (WArr[i] <= 10,000)
# inp[] : (A, B) 로 이루어진 배열. A 와 B 가 이어져있다는 의미이다.
#
# 상황
#   서로 직접 연결이 되지 않은 점들로 집합을 만든다.
#   해당 집합에 있는 원소들의 가중치의 합을 구한다.
#
# 구하는것
#   가중치 합의 최대값
#
# 풀이
#   임의의 원소를 루트노드로 설정한다.
#     - 그래도 트리 구조는 유지된다.
#   두 함수를 만든다.
#     getIncludeArr(now)
#       - now 를 루트노드로 하며
#       - now 를 포함하는 집합중에서
#       - 가장 가중치 합이 큰 집합을 리턴한다. (array 형태로 리턴)
#     getExcludeArr(now)
#       - now 를 루트노드로 하며
#       - now 를 포함하지 않는 집합 중에서
#       - 가장 가중치 합이 큰 집합을 리턴
#
# 연산량
#   1. 배열에 원소를 추가하는 연산 : O(log N)
#     - 파이썬은 배열의 크기가 오버되면 할당하는 메모리를 2배로 늘린다.
#   2. 배열의 원소들의 가중치를 더하는 연산 : O(N)
#
#   최악의 경우 : 모든 노드들이 일렬로 정렬되어 있는 경우 (자식 노드가 1개만 있는 경우)
#     1번 연산 = N * O(log N) = O(N log N)
#     2번 연산 = N * O(log N) = O(N ^ 2)
#       - 배열의 최대 크기는 N/2 이다. (인접한 원소는 포함되어선 안된다.)
#       - 끝점으로 갈 수록 배열의 크기는 1을 향해 작아진다.
#       - 따라서 배열을 더하는 연산은 N/2 * N/2 = N^2/4 이다.
#     N = 10,000 이므로
#     더하는 연산은 25,000,000 (2천 5백만)번 이루어진다.
#     1억개당 1초로 하면 아슬아슬하게 2초 내로 연산이 이루어진다.         
#

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
WArr = list(map(int, input().split()))
connections = [[] for i in range(N + 1)]

for nn in range(N - 1):
  A, B = map(int, input().split())
  connections[A].append(B)
  connections[B].append(A)
  
def calculate(tempArr):
  return sum(WArr[i - 1] for i in tempArr)

# now 노드를 루트노드로 하며
# now 노드를 포함하는 집합 중에서 가중치가 가장 큰 집합
# parent 는 now 노드의 부모 노드이다.
def getIncludeArr(now, parent):
  
  result = [now]
  
  # now 노드를 포함하는 경우는
  # child 노드를 포함하지 않는 경우밖에 없다.
  for child in connections[now]:
    if child != parent:
      result = result + getExcludeArr(child, now)
      
  return result

# now 노드를 루트노드로 하며
# now 노드를 포함하지 않않는 집합 중에서 가중치가 가장 큰 집합
# parent 는 now 노드의 부모 노드이다.
def getExcludeArr(now, parent):
  result = []
  
  # 자신의 자식 노드마다
  # 해당 노드를 포함하는 경우 vs 포함하지 않는 경우 중에서 최대값인 경우를 고른다.
  for child in connections[now]:
    if child != parent:
      incChild = getIncludeArr(child, now)
      excChild = getExcludeArr(child, now)
      
      if calculate(incChild) > calculate(excChild):
        result = result + incChild
      else:
        result = result + excChild
        
  return result

root = 1
incRoot = getIncludeArr(root, root)
excRoot = getExcludeArr(root, root)

# 정렬한채로 출력해야 한다.
incRoot.sort()
excRoot.sort()

sumInc = calculate(incRoot)
sumExc = calculate(excRoot)

if sumInc > sumExc:
  print(sumInc)
  for num in incRoot:
    output("%d " % num)
else:
  print(sumExc)
  for num in excRoot:
    output("%d " % num)