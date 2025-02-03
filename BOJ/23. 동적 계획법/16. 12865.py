#
# things[i] : i 번째 입력
# weight[i] : i 번째 물건의 무게
# value[i] : i 번째 물건의 가치
#
# maxValue[k] : 배낭에 실은 무게가 k 일때 최대 가치
#   초기값 : maxValue[0] = 0, maxValue[k] = -1 for k > 0
#
# 주어진 입력에서
#   물건 개수 n = 4, 최대 무게 k = 7
#
# 주어진 물건들의 (무게, 가치) 입력은
#   (6, 13)
#   (4, 8)
#   (3, 6)
#   (5, 12)
#
# 0번째 물건에 대해서
#   maxValue[0] = 0, maxValue[6] = 13 이 된다.
#
# 1번째 물건에 대해
#   1번째 물건의 무게를 w, 가치를 v 라 할때
#   maxValue[k] >= 0 에 대해서만 다음을 계산한다.
#     maxValue[k + w] = 최대값(maxValue[k + w], maxValue[k] + v)
#       - maxValue[k] == -1 이라는건 i - 1 번째 물건까지 무게의 조합에서
#         k 라는 무게가 안나왔다는걸 의미한다.
#         따라서 maxValue[k] 가 -1 일때는 계산 안한다.
#   이를 계산하면
#   maxValue[0] = 0, maxValue[4] = 8, maxValue[6] = 13 이 된다.
#     - maxValue[4 + 6] = 21 이지만 4 + 6 은 최대무게인 k = 7을 넘는다.
#     - 따라서 이건 계산도, 저장도 안한다.

# 2번째 물건에 대해
#   2번째 물건의 무게는 3, 가치는 6 이다.
#   maxValue[k] >= 0 인 경우에 대해서만 위 수식을 계산하면
#   maxValue[0] = 0
#     - maxValue[0 + 3] = 최대값(maxValue[0 + 3], maxValue[0] + 6)
#     - maxValue[3] = 6
#   maxValue[4] = 8
#     - maxvalue[4 + 3] = 최대값(maxValue[4 + 3], maxValue[4] + 6)
#     - maxValue[7] = 14
#   maxValue[6] = 13
#     - 6 + 3 > 7, 즉 무게가 초과하기 때문에 계산하지 않는다.
#   최종적으로 maxValue 는
#     maxValue[0] = 0
#     maxValue[3] = 6
#     maxValue[4] = 8
#     maxValue[6] = 13
#     maxValue[7] = 14
#   가 된다.
#
# 나머지 물건에 대해서도 반복작업을 하면된다.
# 

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

things = [list(map(int, input().split())) for i in range(n)]
weight = [things[i][0] for i in range(n)]
value = [things[i][1] for i in range(n)]

maxValue = [-1 for i in range(k + 1)]
maxValue[0] = 0

for i in range(n):
  w = weight[i]
  v = value[i]
  for j in range(k + 1 - w):
    if maxValue[k - w - j] >= 0:
      maxValue[k - j] = max(maxValue[k - j], maxValue[k - w - j] + v)
  
print(max(maxValue))