#
# N : 지도의 행의 크기
# M : 지도의 열의 크기
# mapMatrix[][] : 땅이면 1, 물이면 0
#
# 상황
#   상하좌우로 인접한 땅은 같은 섬에 있다.
#   섬들 사이를 다리로 연결하려고 한다.
#     - 다리는 일직선이어야 한다.
#     - 다리의 길이는 2 이상이어야 한다.
#     - 가로로 놓여진 다리는 좌우 끝에 연결된 섬만 이어준다.
#     - 세로도 마찬가지이다.
#
# 구하는것
#   모든 섬들을 연결하기 위한 최소한의 다리 길이
#   연결 못하면 -1을 출력한다.
#
# 풀이
#   1. DFS 로 연결된 땅들을 하나의 섬으로 묶는다.
#   2. 섬과 섬 사이를 연결할 수 있다면 최단거리를 구한다.
#     - 모든 땅에 대해서 4방향마다 이동을 한다.
#     - 만약 땅을 만났을때
#       If 사이에 물이 2칸이상 있고, 다른 섬에 포함된 땅일때
#         - 두 섬간의 최단거리를 갱신한다.
#       더이상 해당 방향으로는 진행하지 않는다.
#   3. 크루스칼 알고리즘(최소 스패닝 트리 구하기)을 이용하여 모든 섬들을 연결하는
#     최소한의 비용을 구한다.
#

import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mapMatrix = [list(map(int, input().split())) for i in range(N)]

islandNumberArr = [[-1 for i in range(M)] for j in range(N)]
distanceArr = [[10 ** 9 for i in range(100)] for j in range(100)]

def dfs(row, col, nowNumber):
  global N, M
  islandNumberArr[row][col] = nowNumber
  
  if row > 0 and mapMatrix[row - 1][col] and islandNumberArr[row - 1][col] == -1:
    dfs(row - 1, col, nowNumber)
  if row < N - 1 and mapMatrix[row + 1][col] and islandNumberArr[row + 1][col] == -1:
    dfs(row + 1, col, nowNumber)
  if col > 0 and mapMatrix[row][col - 1] and islandNumberArr[row][col - 1] == -1:
    dfs(row, col - 1, nowNumber)
  if col < M - 1 and mapMatrix[row][col + 1] and islandNumberArr[row][col + 1] == -1:
    dfs(row, col + 1, nowNumber)
    
newNumber = 0
# 접해있는 땅들을 하나의 섬으로 묶기
for row in range(N):
  for col in range(M):
    if mapMatrix[row][col] == 1 and islandNumberArr[row][col] == -1:
      dfs(row, col, newNumber)
      newNumber += 1
      
# 섬들간의 거리를 구한다.
for row in range(N):
  for col in range(M):
    nowNumber = islandNumberArr[row][col]
    
    # 위로 올라가면서 땅 찾기
    for i in range(1, row + 1):
      if mapMatrix[row - i][col] == 1:
        thisNumber = islandNumberArr[row - i][col]
        if i >= 3 and nowNumber != thisNumber:
          distanceArr[nowNumber][thisNumber] = min(
            distanceArr[nowNumber][thisNumber],
            i - 1
          )
          distanceArr[thisNumber][nowNumber] = min(
            distanceArr[thisNumber][nowNumber],
            i - 1
          )
        break
      
    # 아래로 내려가면서 땅 찾기
    for i in range(row + 1, N):
      if mapMatrix[i][col] == 1:
        thisNumber = islandNumberArr[i][col]
        if i - row >= 3 and nowNumber != thisNumber:
          distanceArr[nowNumber][thisNumber] = min(
            distanceArr[nowNumber][thisNumber],
            i - row - 1
          )
          distanceArr[thisNumber][nowNumber] = min(
            distanceArr[thisNumber][nowNumber],
            i - row - 1
          )
        break
      
    # 왼쪽으로 가면서 땅 찾기
    for i in range(1, col + 1):
      if mapMatrix[row][col - i] == 1:
        thisNumber = islandNumberArr[row][col - i]
        if i >= 3 and nowNumber != thisNumber:
          distanceArr[nowNumber][thisNumber] = min(
            distanceArr[nowNumber][thisNumber],
            i - 1
          )
          distanceArr[thisNumber][nowNumber] = min(
            distanceArr[thisNumber][nowNumber],
            i - 1
          )
        break
      
    # 오른쪽으로 가면서 땅 찾기
    for i in range(col + 1, M):
      if mapMatrix[row][i] == 1:
        thisNumber = islandNumberArr[row][i]
        if i - col >= 3 and nowNumber != thisNumber:
          distanceArr[nowNumber][thisNumber] = min(
            distanceArr[nowNumber][thisNumber],
            i - col - 1
          )
          distanceArr[thisNumber][nowNumber] = min(
            distanceArr[thisNumber][nowNumber],
            i - col - 1
          )
        break

nextVisit = [(0, 0)]
isVisit = [0 for i in range(newNumber)]
result = 0

while len(nextVisit) > 0:
  dist, nowIsland = heapq.heappop(nextVisit)
  
  if isVisit[nowIsland] != 0:
    continue
  
  for nextIsland in range(newNumber):
    if distanceArr[nowIsland][nextIsland] != 10 ** 9 and isVisit[nextIsland] == 0:
      heapq.heappush(nextVisit, (distanceArr[nowIsland][nextIsland], nextIsland))
  
  isVisit[nowIsland] = 1
  result += dist
  
for i in range(newNumber):
  if isVisit[i] == 0:
    result = -1
    break
  
print(result)
