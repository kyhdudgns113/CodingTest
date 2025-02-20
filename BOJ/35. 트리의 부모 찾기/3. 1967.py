# n : 점의 갯수 (n <= 100,000)
# inp[] : (부모, 자식, 거리) 의 배열. 크기는 n - 1
#
# 구하는것
#   트리 구조에서 가장 먼 두 점(노드) 사이의 거리를 구한다.
#
# 풀이
#   부모가 없는 점을 찾고 루트노드로 설정한다.
#   cal(now)
#     - 자식 노드로 내려가는 길 중에서 가장 먼 거리를 리턴
#     - 모든 자식 노드(child) 에 대하여
#       - cal(child) + dist(now, child) 를 배열에 넣는다
#     - 배열을 내림차순으로 정렬하고 다음 경우에 따라 연산한다.
#       Case 1. 배열의 크기가 0
#         - 0을 리턴한다.
#       Case 2. 배열의 크기가 1
#         - 구하려는 최대값과 배열의 값을 비교하여 큰 값으로 갱신한다.
#         - 배열의 값을 리턴한다.
#       Case 3. 배열의 크기가 2 이상
#         - 배열에서 가장 큰 2개의 숫자를 더한값과 최대값을 비교한다.
#         - 배열에서 가장 큰 값 1개를 리턴한다.
#   cal(now) 로 인해 갱신된 최대값을 출력한다.
#
# 연산량
#   1. 모든 점에 대해서 cal(children) + dist 연산 : O(n)
#   2. 배열 내림차순 정렬 : O(n log n)
#     - 한 번 정렬된 배열의 원소는 두 번 다시 정렬에 사용되지 않는다.
#     - 따라서 배열 정렬할때 최악의 경우는 O(n log n) 이다.
#   
#   1 + 2 = O(n log n) = 최대 몇백만
#   
#   

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

childrens = [[] for i in range(n + 1)]
parents = [-1 for i in range(n + 1)]

for i in range(n - 1):
  parent, children, dist = map(int, input().split())
  childrens[parent].append([children, dist])
  parents[children] = parent

globalResult = 0

def calSonAndGetMaxDepth(now):
  global globalResult
  
  resultArr = []
  
  for children, dist in childrens[now]:
    resultArr.append(calSonAndGetMaxDepth(children) + dist)
  
  resultArr.sort()
  resultArr.reverse()
  lenArr = len(resultArr)
  
  result = 0
  if lenArr == 0:
    result = 0
  elif lenArr == 1:
    result = resultArr[0]
  else:
    result = resultArr[0] + resultArr[1]
  globalResult = max(globalResult, result)
  
  return resultArr[0] if lenArr > 0 else 0

# 루트노드 찾기기
rootIdx = 0
for i in range(1, n + 1):
  if parents[i] == -1:
    rootIdx = i
    break

calSonAndGetMaxDepth(rootIdx)

print(globalResult)
