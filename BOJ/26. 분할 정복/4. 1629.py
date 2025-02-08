# a, b, c = 숫자
#
# 구하는것
#   (a ^ b) % c
#
# 조건
#   b <= 2^31 - 1 = 대략 21억
#
# 풀이
#   배열에 다음을 저장한다.
#     abc[0] = a ^ 1 을 c 로 나눈 나머지
#     abc[1] = a ^ 2 를 c 로 나눈 나머지
#     abc[2] = a ^ 4 를 c 로 나눈 나머지
#           ...
#   임의의 입력쌍 10 11 12 에 대하여
#     (a ^ b) % c
#     = (10 ^ 11) % 12
#     = (10 ^ 8 * 10 ^ 2 * 10 ^ 1) % 12
#     = abc[3] * abc[1] * abc[0] % c
#     이렇게 구할 수 있다.

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

abc = [a % c]

numToB = 2
while numToB <= b:
  temp = abc[-1]
  abc.append((temp * temp) % c)
  numToB *= 2
  
result = 1
removeValue = 1
idx = 0
while b > 0:
  if b % 2 == 1:
    result = (result * abc[idx]) % c
  idx += 1
  b //= 2

print(result)