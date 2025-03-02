#
# N : 도시의 수 (N < 1,000)
# RGBArr[][] : 각 도시를 R, G, B 로 칠했을때 발생하는 코스트
#
# 상황
#   도시들은 원형으로 연결 되어있다.
#     = 시작도시와 끝 도시가 연결 되어있다.
#   인접한 도시는 다른 색으로 칠해야 한다.
#
# 구하는것
#   모든 도시를 칠하는 코스트의 최소값
#
# 풀이
#   costArr[시작색깔][현재색깔][현재인덱스]
#     0 번째 도시를 "시작샐깔" 로 칠하고
#     "현재인덱스" 도시를 "현재색깔" 로 칠했을때
#     코스트의 최소값
#     으로 정의한다.
#   now 가 마지막 도시가 아니라면
#     cost[first][color][now] = min(
#       cost[first][다른색 1][now - 1]
#       cost[first][다른색 2][now - 1]
#     ) + RGBArr[now][color] 이다.
#   now 가 마지막 도시이면 min 함수 내에 있는 값 중에서
#     다른색 == 첫번째 색
#   인 경우를 빼면 된다.
#
#   위 점화식은 Bottom-Up 방식으로 풀 수 있다.
#
# 연산량
#   모든 시작 색깔의 경우에 대해서 : 3
#   모든 현재 색깔의 경우에 대해서 : 3
#   모든 도시들에 대해 연산을 한다 : N
#     = O(9N)
#     = 9천
#   이는 0.5초 안에는 무조건 돌아간다.

import sys

input = sys.stdin.readline

N = int(input())

RGBArr = [list(map(int, input().split())) for i in range(N)]

# costArr[i][j][k]
#   0 번째 집이 i 로 칠해져 있고
#   k 번째 집이 j 로 칠해져 있을때
#   코스트의 최소값
costArr = [[[10 ** 9 for i in range(N)] for j in range(3)] for k in range(3)]

costArr[0][0][0] = RGBArr[0][0]
costArr[1][1][0] = RGBArr[0][1]
costArr[2][2][0] = RGBArr[0][2]

for now in range(N - 1):
  next = now + 1
  
  if now != N - 2:
    for firstColor in range(3):
      costArr[firstColor][0][next] = min(
        costArr[firstColor][1][now],
        costArr[firstColor][2][now]
      ) + RGBArr[next][0]
      
      costArr[firstColor][1][next] = min(
        costArr[firstColor][2][now],
        costArr[firstColor][0][now]
      ) + RGBArr[next][1]
      
      costArr[firstColor][2][next] = min(
        costArr[firstColor][0][now],
        costArr[firstColor][1][now]
      ) + RGBArr[next][2]
  else:
    for firstColor in range(3):
      for nextColor in range(3):
        for nowColor in range(3):
          if nextColor != nowColor and nextColor != firstColor:
            costArr[firstColor][nextColor][next] = min(
              costArr[firstColor][nextColor][next],
              costArr[firstColor][nowColor][now] + RGBArr[next][nextColor]
            )
            
result = 10 ** 9
for firstColor in range(3):
  for lastColor in range(3):
    result = min(result, costArr[firstColor][lastColor][N - 1])
    
print(result)

