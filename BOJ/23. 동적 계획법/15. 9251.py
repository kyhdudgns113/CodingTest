#
# A, B : 입력 string
# a : A 의 인덱스
# b : B 의 인덱스
# lcs[a][b] = 
#   max(
#     lcs[a - 1][b],
#     lcs[a][b - 1],
#     lcs[a - 1][b - 1] + 1 if A[a] == B[b]
#   )
#

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())
lena = len(A)
lenb = len(B)

lcsLenArr = [[-1 for i in range(lenb)] for j in range(lena)]

def lcsLen(a, b):
  if a < 0 or b < 0:
    return 0
  
  if lcsLenArr[a][b] >= 0:
    return lcsLenArr[a][b]
  
  if a == 0 and b == 0:
    lcsLenArr[0][0] = 1 if A[a] == B[b] else 0
    return lcsLenArr[0][0]
  one_if_Aa_Bb_same = 1 if A[a] == B[b] else 0
  lcsLenArr[a][b] = max(lcsLen(a - 1, b), lcsLen(a, b - 1), lcsLen(a - 1, b - 1) + one_if_Aa_Bb_same)
  return lcsLenArr[a][b]

print(lcsLen(lena - 1, lenb - 1))  