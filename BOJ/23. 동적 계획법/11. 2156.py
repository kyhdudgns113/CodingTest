# drink[n] : n 번째 음료를 마셨을때 총 마신 양의 최대값
# drink_jump0[n] : n, (n - 1) 번째 음료 마셨을때의 최대값
# drink_jump1[n] : n, (n - 2) 번째 음료 마셨을때의 최대값
# drink_jump2[n] : n, (n - 3) 번째 음료 마셨을때의 최대값
# drink_jump3[n] : 이건 세지 않는다.
#                  n, n - 2, n - 4 마시는 경우 냅두고
#                  n, n - 4 이렇게 마실 이유가 없다.
# drink[n] = max(drink_jump0[n], drink_jump1[n], drink_jump2[n])
#
# maxDrink : 최대로 마신 양
# maxDrink = max(drink[n], drink[n - 1], ... drink[1])
# (사실 n - 1 까지만 내려가도 된다.)
# n - 2 까지만 먹을바에야 n 도 먹는게 맞기 때문이다.

import sys

input = sys.stdin.readline

n = int(input())

wines = list(int(input()) for i in range(n))

drink_jump0 = [0 for i in range(n)]
drink_jump1 = [0 for i in range(n)]
drink_jump2 = [0 for i in range(n)]

drink_jump0[0] = wines[0]
maxDrink = drink_jump0[0]

if n > 1:
  drink_jump0[1] = wines[0] + wines[1]
  drink_jump1[1] = wines[1]
  maxDrink = drink_jump0[1]

if n > 2:
  drink_jump0[2] = wines[1] + wines[2]
  drink_jump1[2] = wines[0] + wines[2]
  drink_jump2[2] = wines[2]
  maxDrink = max(maxDrink, drink_jump0[2], drink_jump1[2])
  
for i in range(3, n):
  drink_jump0[i] = max(drink_jump1[i - 1], drink_jump2[i - 1]) + wines[i]
  drink_jump1[i] = max(drink_jump0[i - 2], drink_jump1[i - 2], drink_jump2[i - 2]) + wines[i]
  drink_jump2[i] = max(drink_jump0[i - 3], drink_jump1[i - 3], drink_jump2[i - 3]) + wines[i]
  maxDrink = max(maxDrink, drink_jump0[i], drink_jump1[i], drink_jump2[i])
  
print(maxDrink)
  