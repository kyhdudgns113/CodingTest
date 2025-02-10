# pypy 로 돌려야 시간초과가 안나온다.
#
# n : 2차원 배열의 갯수
# rc[] : 2차원 행렬의 [row 크기, col크기] 의 배열
#     rc[i][1] == rc[i + 1][0] 임.
#
# 상황
#   2차원 행렬들을 임의의 순서로 곱한다.
#
# 구하는것
#   2차원 행렬들을 전부 곱할때 필요한 최소한의 곱셈 연산 수
#
# 풀이
#   1. [a, b] [b, c] 인 두 행렬을 곱할때는
#       a * b * c 만큼의 곱셈이 필요하다.
#   2. [a, b] [b, c] 두 행렬을 곱하면
#       [a, c] 행렬이 완성된다.
#   3. f(start, end) : start 번째 행렬부터 end 번째 행렬까지 곱할때
#       필요한 곱셈 갯수의 최소값
#   4. f(start, end) = min(sum(
#         (start, mid) 까지의 최소 갯수
#         (mid + 1, end) 까지의 최소 갯수
#         (start, mid)까지 곱한 행렬, (mid + 1, end) 까지 곱한 행렬
#           두 행렬을 곱할때 필요한 곱셈의 갯수
#       ))
#
#   5. f(start, end) = min(
#         f(start, mid) + f(mid + 1, end) +
#         rc[start][0] * rc[mid][1] * rc[end][1]
#       )

import sys

input = sys.stdin.readline

constant = 0x7fffffff

n = int(input())
rc = [list(map(int, input().split())) for i in range(n)]

numMul = [[constant for i in range(n)] for j in range(n)]

def getMinNum(start, end):
  if start == end:
    numMul[start][end] = 0
    return 0
  if start + 1 == end:
    numMul[start][end] = rc[start][0] * rc[start][1] * rc[end][1]
    return numMul[start][end]
  if numMul[start][end] != constant:
    return numMul[start][end]
  
  for mid in range(start, end):
    numMul[start][end] = min(
      numMul[start][end],
      getMinNum(start, mid) + getMinNum(mid + 1, end) + 
      rc[start][0] * rc[mid][1] * rc[end][1]
    )
  return numMul[start][end]


print(getMinNum(0, n - 1))