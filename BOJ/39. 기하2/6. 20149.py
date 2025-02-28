#
# 선분 2개의 꼭지점 좌표가 주어진다.
#
# 상황
#   점 3개 이상이 일직선에 있는 경우도 있다.
#
# 구하는것
#   교점이 있으면 1, 없으면 0 출력
#   교점이 하나면 교점의 좌표를 출력력
#
# 풀이
#   1. 교점이 있는지 확인
#     점 1, 2 가 하나의 선분, 점 3, 4 가 하나의 선분을 이룬다고 둔다.
#     132, 142, 314, 324 순서로 선적분한 결과를 각각 구한다.
#     132 와 142 의 선적분 값이 둘 다 양수거나 음수면 교점이 없는것이다.
#     둘 다 부호가 다르거나 둘 중 하나가 0 이면
#       - 두 선분의 기울기가 다르다
#       - 교점이 있다
#     둘 다 0 이면 점 4개가 일직선에 있다는 것이다.
#       - x 좌표와 y 좌표의 크기를 비교하여 교점이 있는지 알 수 있다.
#   2. 교점의 좌표
#     모든 점이 일직선에 있는 경우
#       교점이 하나일때 출력한다.
#       교점이 하나인지 여부는 1번 단계에서 확인한다.
#     두 선분의 기울기가 다른 경우
#       크레이머 공식으로 교점의 좌표를 구한다
#
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def getArea(x0, y0, xm, ym, xz, yz):
  area0m = (xm - x0) * (ym + y0)
  areamz = (xz - xm) * (yz + ym)
  areaz0 = (x0 - xz) * (y0 + yz)
  
  return area0m + areamz + areaz0

area132 = getArea(x1, y1, x3, y3, x2, y2)
area142 = getArea(x1, y1, x4, y4, x2, y2)
area314 = getArea(x3, y3, x1, y1, x4, y4)
area324 = getArea(x3, y3, x2, y2, x4, y4)

diff12 = 0
diff34 = 0

#
# 기울기가 다르면서 교점이 있는지 확인하는 부분
#
if area132 >= 0 and area142 < 0 or \
  area132 > 0 and area142 <= 0 or \
  area132 <= 0 and area142 > 0 or \
  area132 < 0 and area142 >= 0:
  diff12 = 1
  
if area314 >= 0 and area324 < 0 or \
  area314 > 0 and area324 <= 0 or \
  area314 <= 0 and area324 > 0 or \
  area314 < 0 and area324 >= 0:
  diff34 = 1
  
isSameLine = False
isMultiple = False

#
# 일직선에 있으면서 교점이 있는지 확인하는 부분
#
if area132 == 0 and area142 == 0 and area314 == 0 and area324 == 0:
  isSameLine = True
  diff12 = 1
  diff34 = 1
  
  xx1, xx2 = min(x1, x2), max(x1, x2)
  xx3, xx4 = min(x3, x4), max(x3, x4)
  
  # 일직선에 있는데 교점은 없는지 확인하는 부분
  # 점들의 x 좌표가 전부 같은 경우는 여기서 캐치하지 못한다.
  if xx1 < xx2 < xx3 < xx4 or xx3 < xx4 < xx1 < xx2:
    diff12 = 0
    diff34 = 0
  
  # 일직선에 있는데 교점은 없는지 확인하는 부분
  # 점들의 x 좌표가 전부 같은 경우는 여기서 캐치한다.
  yy1, yy2 = min(y1, y2), max(y1, y2)
  yy3, yy4 = min(y3, y4), max(y3, y4)
  if yy1 < yy2 < yy3 < yy4 or yy3 < yy4 < yy1 < yy2:
    diff12 = 0
    diff34 = 0
    
  if xx1 <= xx3 < xx2 or xx1 < xx4 <= xx2 or yy1 <= yy3 < yy2 or yy1 < yy4 <= yy2:
    isMultiple = True


if diff12 == 1 and diff34 == 1:
  print(1)
  if isSameLine and isMultiple == False:
    if x1 == x3 and y1 == y3:
      print(x1, y1)
    elif x1 == x4 and y1 == y4:
      print(x1, y1)
    elif x2 == x3 and y2 == y3:
      print(x2, y2)
    elif x2 == x4 and y2 == y4:
      print(x2, y2)
  elif isSameLine == False:
    A1, B1 = (y2 - y1), (x1 - x2)
    A2, B2 = (y4 - y3), (x3 - x4)
    C1, C2 = (A1*x1 + B1*y1), (A2*x3 + B2*y3)
    D = A1*B2 - A2*B1
    
    x = (C1*B2 - C2*B1)/D
    y = (A1*C2 - A2*C1)/D
    print(x, y)
    
else:
  print(0)