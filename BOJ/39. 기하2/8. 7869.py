#
# 상황
#   2차원 좌표에서 두 원의 중심좌표, 반지름이 주어진다.
#
# 구하는것
#   겹치는 부분의 넓이
#
# 풀이
#   수식을 이용하여 풀었다.
# 

import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if min(r1, r2) + d <= max(r1, r2):
  r3 = min(r1, r2)
  if r3 == 0:
    print("0.000")
  else:
    print("%.3f" % r3*r3*math.pi)
elif r1 > 0 and r2 > 0 and r1 + r2 > d:
  r1cos = (r1*r1 - r2*r2 + d*d) / (2*d)
  h = math.sqrt(r1*r1 - r1cos*r1cos)

  acosr1 = math.acos(r1cos/r1)
  acosr2 = math.acos((d - r1cos)/r2)

  r1area = r1*r1*acosr1
  r2area = r2*r2*acosr2

  sharedArea = d * h

  result = r1area + r2area - sharedArea

  print("%.3f" % result)
else:
  print("0.000")