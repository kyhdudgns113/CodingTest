#
# N : 수의 갯수 (N <= 15)
# numbers[] : 수의 배열. numbers[i] 는 십진법으로 길이는 최대 50이다.
# K : 나누는 값 (K <= 100)
#
# 상황
#   numbers[] 에 있는 숫자들을 일렬로 연결하여 수를 만든다.
#     {1, 32, 4} 면 1324, 1432, 3214 등등...
#
# 구하는것
#   만든 수가 K 로 나누어 떨어질 확률을 기약분수 형태로 출력한다.
#     경우의 수가 0이면 0/1
#
# 풀이
#   모든 경우를 다 세면 N! 로 1억을 한참 초과한다.
#   비트마스크를 이용하여 풀 수 있다.
#
#   cntArr[k][bitMask] : bitMask 에 표시된 숫자들을 사용하여
#     나머지가 k 인 숫자를 만드는 경우의 수
#
#     numbers = {12, 3, 4}, K = 100 이라 하자.
#     숫자 12 만 사용하여 나머지가 12 가 되는 경우의 수는 1이다.
#       = cntArr[12][0x100] = 1
#     이 뒤에 3을 추가하면 나머지가 23이 된다.
#     즉, 나머지가 23이며, bitMask 가 0x110 인 경우의 수는
#     cntArr[12][0x100] 만큼 더해줄 수 있다는 뜻이 된다.
#       = cntArr[23][0x110] += cntArr[12][0x100]
#     이를 Dynamic Programming 의 Bottom-Up 방식으로 풀면 된다.
#
# 연산량
#   모든 비트마스크에 대하여 : 2 ^ N
#   모든 숫자만큼 확인을 하고 : N
#   모든 나머지의 경우마다 연산을 한다 : K
#     = O(N*K*2^N)
#     = 4900 만
#   간신히 1억이 안되므로 연산 최적화를 어느정도 해줘야 한다.
#

import sys, math

input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for i in range(N)]
K = int(input())

NFactorial = math.factorial(N)

cntArr = [[0 for i in range(2 ** N)] for j in range(K)]

# num 의 10진법 길이이
def getLen(num):
  result = 0
  while num > 0:
    result += 1
    num //= 10
  return result

lenArr = [getLen(numbers[i]) for i in range(N)]

# 나머지가 baseModular 인 숫자에서 numbers[idx] 를 뒤에 추가했을때
# 그 값을 K 로 나눈 나머지지
def getModular(baseModular, idx):
  global K
  
  numLen = lenArr[idx]
  
  result = baseModular
  for i in range(numLen):
    result *= 10
    result %= K
    
  result += numbers[idx]
  result %= K
  
  return result


cntArr[0][0] = 1

# 저장 안하고 그때그때 계산하면 중복연산 및 시간초과가 생긴다.
modularArr = [[getModular(baseModular, idx) for idx in range(N)] for baseModular in range(K)]

for bitMask in range(2 ** N):
  for next in range(N):
    if bitMask & (2 ** next) == 0:
      newMask = bitMask + (2 ** next)
      for modular in range(K):
        newModular = modularArr[modular][next]
        cntArr[newModular][newMask] += cntArr[modular][bitMask]
        
result = cntArr[0][-1]

if result == 0:
  print("0/1")
elif result == NFactorial:
  print("1/1")
else:
  gcdVal = math.gcd(result, NFactorial)
  print("%d/%d" % (result//gcdVal, NFactorial//gcdVal))

        
