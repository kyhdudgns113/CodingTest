#
# 선분 2개의 좌표가 선분마다 다른 줄로 입력값이 된다.
#
# 상황
#   점 3개가 일직선인 경우는 없다
#
# 구하는것
#   선분의 교점이 있으면 1, 없으면 0을 출력한다.
#
# 풀이
#   선분 1을 구성하는 점을 1, 2
#   선분 2를 구성하는 점을 3, 4 라고 하자.
#   
#   직선의 방정식을 만들고 그들의 교점을 구하여 해당 교점이 선분을 지나는지 확인하는 방법도 있다.
#     - 쓸데없이 복잡해진다.
#
#   두 선분이 교점이 존재할때 다음이 성립한다.
#     - 점 132의 선적분값의 부호와 점 142의 선적분값의 부호가 다르다
#     - 점 214의 선적분값의 부호와 점 234의 선적분값의 부호가 다르다
#     위 2개 전부 만족하면 선분의 교점이 존재한다.
#

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def getArea(x0, y0, xm, ym, xz, yz):
  area0m = (xm - x0) * (ym + y0) / 2
  areamz = (xz - xm) * (yz + ym) / 2
  areaz0 = (x0 - xz) * (y0 + yz) / 2
  
  return area0m + areamz + areaz0

sign132 = 1 if getArea(x1, y1, x3, y3, x2, y2) > 0 else 0
sign142 = 1 if getArea(x1, y1, x4, y4, x2, y2) > 0 else 0

sign314 = 1 if getArea(x3, y3, x1, y1, x4, y4) > 0 else 0
sign324 = 1 if getArea(x3, y3, x2, y2, x4, y4) > 0 else 0

if sign132 != sign142 and sign314 != sign324:
  print(1)
else:
  print(0)
  