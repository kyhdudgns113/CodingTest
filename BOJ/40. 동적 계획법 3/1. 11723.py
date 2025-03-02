#
# M : 쿼리의 갯수 (M <= 3,000,000)
# inp[] : 쿼리의 배열
#   add x : 집합 S 에 x (1 <= x <= 20) 를 없으면면 추가한다.
#   remove x : 집합 S 에서 x 가 있으면면 제거한다.
#   check x : 집합 S 에 x 가 있으면 1, 없으면 0을 출력한다.
#   toggle x : 집합 S 에 x 가 있으면 빼고, 없으면 추가한다.
#   all : 집합 S 를 {1, 2, 3 ... 20} 으로 만든다.
#   empty : 집합 S 를 공집합으로 바꾼다.
#
# 구하는것
#   알맞은 값을 출력한다.
#
# 풀이
#   비트마스크를 이용하여 풀 수 있다
#

import sys

input = sys.stdin.readline
output = sys.stdout.write

bitmask = 0

M = int(input())

for mm in range(M):
  inp = list(map(str, input().strip().split()))
  order = ""
  num = 0
  if len(inp) == 2:
    order, num = inp
  else:
    order = inp[0]
  num = int(num)
  
  if order == "add":
    bitmask |= 2 ** num
  elif order == "remove":
    bitmask &= ~(2 ** num)
  elif order == "check":
    if (bitmask & (2 ** num)) > 0:
      output("1\n")
    else:
      output("0\n")
  elif order == "toggle":
    bitmask ^= 2 ** num
  elif order == "all":
    bitmask = 0x7fffffff
  else:
    bitmask = 0