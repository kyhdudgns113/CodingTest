# N*N 행렬 A 에 대하여
# A^B 의 모든 요소를 1000 으로 나눈 나머지 행렬을 구하면 된다.
#
# B 가 매우 크므로
# A^1, A^2, A^4, A^8 .... 등을 저장하여 분할정복으로 풀면 된다. 

import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(N))

for i in range(N):
  for j in range(N):
    A[i][j] %= 1000

AexpK = [A]
temp = 1
while temp <= B:
  Ak2 = [[0 for i in range(N)] for j in range(N)]
  Ak = AexpK[-1]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        Ak2[i][j] += Ak[i][k] * Ak[k][j]
        Ak2[i][j] %= 1000
  AexpK.append(Ak2)
  temp *= 2

idx = 0
AexpB = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

while B > 0:
  if B % 2 == 1:
    AA = AexpK[idx]
    tempAB = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
      for j in range(N):
        for k in range(N):
          tempAB[i][j] += AexpB[i][k] * AA[k][j]
          tempAB[i][j] %= 1000
    AexpB = tempAB.copy()
  B //= 2
  idx += 1
  
for row in AexpB:
  print(*row)
  