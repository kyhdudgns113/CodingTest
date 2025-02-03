#
# stairs[n] : n 번째 계단의 점수수
#
# n 번째 계단을 밟았을때의 상태는 다음 2가지로 나뉠 수 있다.
#   1. scorePrev[n] : 이전 계단에서 한 계단 밟은 경우
#   2. scoreJump[n] : 두단계 이전 계단에서 점프한 경우
#
# 1. scorePrev[n] = 
#     max(
#       scorePrev[n - 1] (= 0, 계단을 3개연속 밟을 수 없다)
#       scoreJump[n - 1]
#     ) + stairs[n]
#     = scoreJump[n - 1] + stairs[n]
#
# 2. scoreJump[n] =
#     max(
#       scorePrev[n - 2],
#       scoreJump[n - 2]
#     ) + stairs[n]
#
# 이를 bottom-up 방식으로 풀었다.
# 특별히 Top-Down 방식 대신 Bottom-Up 으로 푼 이유는 없다.

import sys

input = sys.stdin.readline

n = int(input())

stairs = [int(input()) for i in range(n)]

scorePrev = [0 for i in range(n)]
scoreJump = [0 for i in range(n)]

scorePrev[0] = stairs[0]

if n > 1:
  scorePrev[1] = scorePrev[0] + stairs[1]
  scoreJump[1] = stairs[1]
  
for i in range(2, n):
  scorePrev[i] = scoreJump[i - 1] + stairs[i]
  scoreJump[i] = max(scorePrev[i - 2], scoreJump[i - 2]) + stairs[i]

print(max(scorePrev[n - 1], scoreJump[n - 1]))