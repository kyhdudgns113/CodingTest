#
# pypy 로 돌려야 한다.
#
# A, B : 두 문자열
#
# 상황
#   A, B 와 동시에 부분수열이 되는것 중에서 가장 긴 수열을 구한다.
# 
# 구하는것
#   - 가장 긴 것의 길이
#   - 가장 긴 부분 수열중 하나
#
# 풀이
#   LCS[ia][ib] : ia 번째와 ib 번째 문자열까지 가장 긴 부분 수열
#   LCS[ia][ib] = max(
#       LCS[ia - 1][ib],
#       LCS[ia][ib - 1],
#       LCS[ia - 1][ib - 1]
#     ) 이다.
#
#   LCS[ia][ib] 값은 한 번 계산하면 저장한다.
#   그러면 그 이후에는 LCS[ia][ib] 를 계산하기 위해
#   LCS[ia - 1][ib], LCS[ia][ib - 1] 등을 또 계산할 필요가 없어진다.

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

lenA = len(A)
lenB = len(B)

lcs = []
lcsLen = [[-1 for i in range(lenB)] for j in range(lenA)]

def recurse(ia, ib):
  a = A[ia]
  b = B[ib]
  
  if ia == 0 and ib == 0:
    if a == b:
      return a
    else:
      return ""
    
  if lcsLen[ia][ib] != -1:
    return lcsLen[ia][ib]
    
  result = ""
  
  # 두 문자가 같으면 인덱스를 둘 다 1 낮춰야 한다.
  # 안그러면 중복하여 구하게 된다.
  #   ex) ABCD"D" ABC"D"
  #     ia 만 1 낮추면 D 와 D 가 또 만나게 된다.
  if a == b:
    if ia > 0 and ib > 0:
      result = recurse(ia - 1, ib - 1)
    result = result + a
  else:
    ia1 = ""
    ib1 = ""
    iab = ""
    
    if ia > 0:
      ia1 = recurse(ia - 1, ib)
    if ib > 0:
      ib1 = recurse(ia, ib - 1)
    if ia > 0 and ib > 0:
      iab = recurse(ia - 1, ib - 1)
    
    if len(ia1) >= len(ib1) and len(ia1) >= len(iab):
      result = ia1
    elif len(ib1) >= len(ia1) and len(ib1) >= len(iab):
      result = ib1
    else:
      result = iab
  
  lcsLen[ia][ib] = result
  return result

result = recurse(lenA - 1, lenB - 1)

print(len(result))
if len(result) > 0:
  print(result)
