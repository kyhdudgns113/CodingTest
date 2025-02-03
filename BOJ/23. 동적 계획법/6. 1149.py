#
# minCost[n][color] : n 번째 집을 color 로 색칠했을때 최소 비용
# minCost[n][color] = 
#   min(
#     minCost[n - 1][다른색 1],
#     minCost[n - 1][다른색 2]
#   ) + cost[n][color] 이다.
# 이번 문제는 재귀로 풀어봤다.

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

costs = [list(map(int, input().split())) for i in range(n)]

minCost = [[0, 0, 0] for i in range(n)]

def recurse(houseIdx, colorIdx):
  if minCost[houseIdx][colorIdx] != 0:
    return minCost[houseIdx][colorIdx]
  if houseIdx == 0:
    minCost[0][colorIdx] = costs[0][colorIdx]
    return costs[0][colorIdx]

  idx1 = (colorIdx + 1) % 3
  idx2 = (colorIdx + 2) % 3
  
  minCost[houseIdx][colorIdx] = min(recurse(houseIdx - 1, idx1), recurse(houseIdx - 1, idx2)) + costs[houseIdx][colorIdx]
  return minCost[houseIdx][colorIdx]
  
print(min(recurse(n - 1, 0), recurse(n - 1, 1), recurse(n - 1, 2)))