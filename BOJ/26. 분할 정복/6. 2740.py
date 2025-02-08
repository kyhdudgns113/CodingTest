# 입력
# N, M : 행렬 A 의 row 와 col
# A[N] : row 가 N 인 행렬 A
# M, K : 행렬 B 의 row 와 col
# B[m] : row 가 M 인 행렬 B
#
# 출력
# A * B
#
# 풀이
#  행렬 곱셈을 그냥 하면 된다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(N))

M, K = map(int, input().split())
B = list(list(map(int, input().split())) for i in range(M))

C = [[0 for i in range(K)] for j in range(N)]

for n in range(N):
  for k in range(K):
    for m in range(M):
      C[n][k] += A[n][m] * B[m][k]

for row in C:
  print(*row)

