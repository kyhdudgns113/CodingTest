# n : 종이의 한 변의 길이
# paper[][] : 종이에 칠해져있는 색(0 : 흰색, 1 : 파란색)
#
# 상황 : 정사각형 모양의 종이를 정사각형 모양으로 4등분 한다.
#       각 부분마다 하나의 색종이로 덮을 수 있으면 그렇게 한다.
#       아닌 부분은 다시 4등분을 하고 위 작업을 반복한다.
# 구하는것 : 흰색 종이의 갯수와 파란색 종이의 갯수를 구한다.
#
# 풀이
#   종이를 4등분 한다.
#   각 부분의 경우를 구한다.
#     1. 흰색으로 덮을 수 있나 (1 리턴)
#     2. 파란색으로 덮을 수 있나 (2 리턴)
#     3. 그 어떠한 걸로도 한번에 덮을수는 없는가 (0 리턴)
#   1 이나 2 면 상위 단계로 결과값을 리턴만 한다.
#   3 이면 각 부분들에 대해 다음 연산을 수행한다.
#     1. 흰색종이면 result[1] += 1
#     2. 파란색 종이면 result[2] += 1
#     3. 둘 다 아니면 result[0] += 1
#       - 불필요한 연산이지만 코드를 간단하게 하기 위해서 실행한다.
#     모든 경우에 대해서 상위 단계로 결과값 0 을 리턴한다.
#

import sys

sys.setrecursionlimit(16)

input = sys.stdin.readline

n = int(input())

paper = list(list(map(int, input().split())) for i in range(n))

result = [0, 0, 0]

# 리턴값
#   0 : 해당 종이는 한 장으로 완성되지 않는다.
#   1 : 해당 종이는 0으로 채워져 있다.
#   2 : 해당 종이는 1로 채워져 있다.
def paperPart(r0, c0, r1, c1):
  global result
  if r0 == r1:
    return 1 + paper[r0][c0]
  
  halfLen = (r1 - r0 + 1) // 2
  
  upLeft = paperPart(r0, c0, r0 + halfLen - 1, c0 + halfLen - 1)
  upRight = paperPart(r0, c0 + halfLen, r0 + halfLen - 1, c1)
  downLeft = paperPart(r0 + halfLen, c0, r1, c0 + halfLen - 1)
  downRight = paperPart(r0 + halfLen, c0 + halfLen, r1, c1)
  
  if upLeft == 1 and upRight == 1 and downLeft == 1 and downRight == 1:
    return 1
  elif upLeft == 2 and upRight == 2 and downLeft == 2 and downRight == 2:
    return 2
  else:
    result[upLeft] += 1
    result[upRight] += 1
    result[downLeft] += 1
    result[downRight] += 1
    return 0
  
result[paperPart(0, 0, n - 1, n - 1)] += 1
  
print(result[1])
print(result[2])
  
