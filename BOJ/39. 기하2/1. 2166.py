#
# N : 2차원 좌표상의 점의 갯수
# points[] : (x, y) 로 구성된 점들의 좌표. 인접한 점들은 연결되어있다.
#
# 상황
#   주어진 점들로 도형을 만든다.
#   인접한 점들끼리는 서로 연결 되어있다.
#   시작점과 끝점도 연결 되어있다.
#
# 구하는것
#   도형의 넓이
#
# 풀이
#   선적분(?)을 하면 된다.
#     연결된 두 점 사이를 적분하고 누적한다.
#     누적합에 절대값을 씌우면 도형의 넓이가 된다.
#

import sys

input = sys.stdin.readline

N = int(input())

points = [list(map(int, input().split())) for i in range(N)]

tempResult = 0

for i in range(N):
  x0, y0 = points[i]
  x1, y1 = points[i + 1] if i < N - 1 else points[0]
  
  tempResult += (x1 - x0) * (y0 + y1) / 2
  
print("%.1f" % abs(tempResult))
