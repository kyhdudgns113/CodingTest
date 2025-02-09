# k : 주어진 랜선의 개수
# n : 목표 갯수
# lines[] : 주어진 랜선의 길이 배열
#
# 상황
#   - 랜선들을 같은 크기의 정수길이만큼 쪼개어 n개 이상을 만든다
#
# 구하는것
#   - 랜선의 최대 길이
#
# 풀이
#   - 0 부터 max(lines) 사이에서 이분탐색으로 찾는다.
#   - c = (l + r) // 2
#   - 길이 c 로 잘랐을때 길이를 numLines 라고 하자.
#   Case 1. numLines < n 이면
#     - 구하려는 길이는 c 보다 무조건 작아야 한다.
#     - 범위를 (l, c - 1) 로 바꾼다.
#   Case 2. numLines >= n 이면
#     - 구하려는 길이는 c 이상이다.
#       - 같은 크기의 랜선은 n 보다 커도 됨을 유념한다.
#     - 범위를 (c, r) 로 바꾼다.
#   

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

k, n = map(int, input().split())

lines = [int(input()) for i in range(k)]

def getLines(val):
  return sum(line // val for line in lines)

def findMaxLine(l, r):
  global n
  if l + 1 == r:
    if getLines(r) >= n:
      return r
    else:
      return l
  if l == r:
    return l
  
  c = (l + r) // 2
  numLines = getLines(c)
  if numLines < n:
    return findMaxLine(l, c - 1)
  else:
    return findMaxLine(c, r)
  
print(findMaxLine(1, max(lines)))

  