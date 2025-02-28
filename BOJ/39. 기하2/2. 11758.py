#
# points[] : (x, y) 로 이루어진 점 3개의 좌표
#
# 상황
#   점 1 에서 점 2로, 그 다음은 점 3으로 이동한다.
#
# 구하는것
#   시계방향으로 이동하면 -1
#   일직선이면 0
#   반시계방향이면 1 을 출력한다.
#
# 풀이
#   점 3개로 만들 수 있는 삼각형을 선적분 한다.
#   넓이가 음수면 반시계 방향이다.
#   일직선이면 넓이가 0이다
#   넓이가 양수면 시계 방향이다.
#

points = [list(map(int, input().split())) for i in range(3)]

dif1 = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
dif2 = [points[2][0] - points[1][0], points[2][1] - points[1][1]]

integral = 0

for i in range(3):
  x0, y0 = points[i]
  x1, y1 = points[i + 1] if i < 2 else points[0]
  
  integral += (x1 - x0) * (y0 + y1) / 2
  

if integral == 0:
  print(0)
elif integral > 0:
  print(-1)
else:
  print(1)

