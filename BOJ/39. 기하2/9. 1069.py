#
# X, Y : 점의 좌표
# D : 점프할 수 있는 거리
# T : 점프할떄 소모하는 시간
#
# 상황
#   (X, Y) 에서 (0, 0) 으로 이동한다.
#   1초당 1만큼 걸어갈 수 있다.
#   점프하여 T초만에 D 만큼 갈 수 있다.
#
# 구하는것
#   도착하는 최단시간 
#

import math

X, Y, D, T = map(int, input().split())

result = 0

R = math.sqrt(X*X + Y*Y)

if D <= T:
  result = R
else:
  while R >= 2*D:
    R -= D
    result += T
  delta = min(R, 2*T, T + abs(R - D))
  result += delta
  
print(result)
  