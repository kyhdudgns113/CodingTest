# n : 나무의 갯수
# m : 남아야 하는 나무 길이의 합
# trees[] : 나무 길이들의 배열
#
# 상황
#   나무들을 각각 길이 x 만큼 잘라낸다.
#   x 보다 작은건 소멸된다
#
# 구하는것
#   남은 나무 길이의 총합이 m 이상이 되도록 하는
#   x 의 최대값을 구한다.
#
# 풀이
#   - trees[] 를 오름차순으로 정렬한다.
#   - l=0 부터 r=10 ** 9 안에서 길이 x 를 찾는다.
#     - c=(l + r) // 2 라 하자
#     - trees 를 c 만큼 잘랐을때의 나머지를 remainTrees 라고 하자
#       Case 1. remainTrees < m:
#         - 남은 나무가 m보다 작은 상황
#         - 자르는 높이를 "무조건" 낮춰야 한다.
#         - 범위를 (l, c - 1) 로 한다.
#       Case 2. remainTrees > m:
#         - 남은 나무가 m 보다는 큰 상황
#         - 자르는 길이가 c 인 경우도 포함해야 한다.
#         - 범위를 (c, r) 로 한다.
#       Case 3. remainTrees == m:
#         - 구하는 정답이다.
#         - c보다 크면 m 보다 작을것이다.
#         - c보다 작은 값은 고려할 필요가 없다. (c 가 최대값이기 때문)
#         - c 를 리턴한다.
#
#   - trees 를 c 만큼 자른 값을 구하기 (def cutTrees(c))
#     - sum((tree - c) for tree in trees) 를 해도 된다.
#     - 하지만 모든 trees 에 대해서 연산을 할 필요는 없다.
#     - trees[i] 값이 c 보다 큰 경우에 대해서만 계산해도 된다.
#     - 정렬된 trees[] 에서 c만큼 자를 수 있는 경우에 대해서만 계산한다.
#     - findIdx 함수를 이용한다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

sumAfter = [0 for i in range(n)]
sumAfter[n - 1] = trees[n - 1]
for i in range(1, n):
  sumAfter[n - 1 - i] = sumAfter[n - i] + trees[n - 1 - i]

# 높이가 c 보다는 큰 trees[] 요소중에서
# 가장 작은 요소의 인덱스를 리턴한다.
def findIdx(c, l, r):
  if l == r:
    return l
  
  cidx = (l + r) // 2
  if trees[cidx] < c:
    return findIdx(c, cidx + 1, r)
  elif trees[cidx] > c:
    return findIdx(c, l, cidx)
  else:
    return cidx

# trees[] 를 높이 c 로 자른 나머지를 구한다.
# trees[] 에서 c 보다 큰 것들만 가지고 계산한다.
def cutTrees(c):
  global n
  idx = findIdx(c, 0, n - 1)
  return sum((tree - c) for tree in trees[idx::])

# trees[] 를 높이 x 만큼 자른다.
# 이 떄 남은 trees 들의 합이 m 이상이어야 한다.
# 이 때 최대 x 를 구한다.
def findMaxHeight(l, r):
  global m
  if l == r:
    return l
  
  if l + 1 == r:
    cutTreeByR = cutTrees(r)
    if cutTreeByR >= m:
      return r
    else:
      return l
  
  c = (l + r) // 2
  if c >= trees[-1]:
    return findMaxHeight(l, c - 1)
  
  remainTrees = cutTrees(c)
  if remainTrees < m:
    return findMaxHeight(l, c - 1)
  elif remainTrees > m:
    return findMaxHeight(c, r)
  else:
    return c
  
print(findMaxHeight(0, 10 ** 9))
