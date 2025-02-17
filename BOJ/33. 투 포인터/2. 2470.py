# n : 수열의 갯수
# a[] : 중복 없는 수열 ( abs(a[i]) <= 1,000,000)
#
# 구하는것
#   a 의 두 수를 더한 절대값이 가장 작은 쌍을 구한다.
#   (a[i], a[j]), (a[i] < a[j])
#
# 풀이
#   a 를 정렬한다.
#   l = 0, r = n - 1 로 두고 a[l], a[r] 의 합과 그 절대값으로 연산을 한다.
#   절대값이 더 작으면 갱신을 한다.
#
#   a[l] + a[r] 이 0보다 크다면 더 작은 절대값을 위해 a[r] 을 줄여야한다.
#     - r 에 1을 뺀다.
#   a[l] + a[r] 이 0보다 작다면 더 작은 절대값을 위해 a[l] 을 키워야 한다.
#     - l 에 1을 더한다.
#   a[l] + a[r] 이 0이면 더 연산을 할 필요가 없다.

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

leftValue = 0
rightValue = 0
minAbs = 2 * (10 ** 9)

l = 0
r = n - 1

while l < r:
  tempSum = a[l] + a[r]
  tempAbs = abs(tempSum)
  
  if minAbs > tempAbs:
    minAbs = tempAbs
    leftValue = a[l]
    rightValue = a[r]
  
  if tempSum > 0:
    r -= 1
  elif tempSum < 0:
    l += 1
  else:
    break

print(leftValue, rightValue)