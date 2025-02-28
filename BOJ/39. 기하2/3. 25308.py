#
# inputArr[] : 능력치의 배열 (8 개)
#
# 상황
#   8개의 능력치가 있으며, 이를 보기 편하게 방사형 그래프로 나타낸다.
#     첫 번째 점은 원점을 기준으로 12시 방향에 둔다.
#     두 번째 점은 원점을 기준으로 1.5시 방향에 둔다.
#     세 번째 점은 3시 방향에 둔다.
#     같은 방식으로 8개를 배치한다.
#   인접한 점들을 이어서 하나의 다각형을 만든다.
#     n 번째 점은 n - 1 번째 점과 n + 1 번째 점과 연결한다.
#     범위를 초과하면 순환하여 연결한다.
#
# 구하는것
#   만들 수 있는 볼록다각형의 갯수
#     - 볼록다각형은 모든 내각이 180도 이내인 다각형을 의미한다.
#     - 같은 도형이 회전한 형태는 각각 다른 경우로 계산한다.
#
# 풀이
#   모든 8개의 능력치의 조합에 대하여 (8! = 40320 개)
#     인접한 3점이 이루는 각도중 원점을 향하는 각도가 180도 이내인지 확인한다.
#       - 단 하나라도 180도가 넘으면 그 도형은 볼록다각형이 아니다.
#     인접한 3점의 내각이 180도 이하라면 그 점을 선적분한 결과가 양수라는 뜻이다.
#       - 양수가 아니면 해당 도형은 볼록 다각형이 아니게 된다.
#
# 연산량
#   모든 8개의 능력치의 조합에 대하여 (40320)
#   로테이션을 돌면서 선적분을 한다(24)
#   = 약 100만
#

from itertools import permutations
import math

inputArr = list(map(int, input().split()))
indexedInput = list(enumerate(inputArr))

entire = list(permutations(indexedInput, 8))

result = 0

for eachCase in entire:
  sqrt2 = math.sqrt(2)
  points = [
    [0, eachCase[0][1]],
    [eachCase[1][1]/sqrt2, eachCase[1][1]/sqrt2],
    [eachCase[2][1], 0],
    [eachCase[3][1]/sqrt2, -eachCase[3][1]/sqrt2],
    [0, -eachCase[4][1]],
    [-eachCase[5][1]/sqrt2, -eachCase[5][1]/sqrt2],
    [-eachCase[6][1], 0],
    [-eachCase[7][1]/sqrt2, eachCase[7][1]/sqrt2]
  ]
  
  tempResult = 1
  for i in range(8):
    x0, y0 = points[i]
    x1, y1 = points[i + 1] if i < 7 else points[0]
    x2, y2 = points[i + 2] if i < 6 else points[0] if i < 7 else points[1]
    
    area1 = (x1 - x0) * (y1 + y0)
    area2 = (x2 - x1) * (y2 + y1)
    area3 = (x0 - x2) * (y0 + y2)
    
    sumArea = area1 + area2 + area3
    
    if sumArea < 0.01:
      tempResult = 0
      break
    
  result += tempResult
  
print(result)