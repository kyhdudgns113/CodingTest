# n : 수열의 갯수 (n <= 100,000)
# a : 길이 n 인 수열 (a[i] <= 1,000,000)
# x : 구하려는 수 (x <= 2,000,000)
#
# 구하는것
#   a[i] + a[j] 을 만족하는 경우의 수 (i < j)
#
# 풀이
#   a 를 오름차순으로 정렬한다
#   양쪽 끝에서 시작한다.
#   두 수를 더하고 경우에 따라 연산한다.
#     x 보다 작을때
#       더한 수가 커져야 한다.
#       왼쪽 인덱스를 1 늘린다.
#     x 보다 클 때
#       더한 수가 작아져야 한다.
#       오른쪽 인덱스를 1 줄인다.
#     둘이 같을때
#       (left, right - 1) 이나 (left + 1, right) 쌍은
#       고려할 필요가 없다. (a[i] 는 중복되지 않는다.)
#       left 를 1 늘리고, right 를 1 줄인다.

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

left = 0
right = n - 1
result = 0

while left < right:
  tempSum = a[left] + a[right]
  if tempSum < x:
    left += 1
  elif tempSum > x:
    right -= 1
  else:
    result += 1
    left += 1
    right -= 1

print(result)