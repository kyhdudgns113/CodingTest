#
# T : 원본 문자열 (최대 길이 1,000,000)
# P : 찾을 문자열 (최대 길이 1,000,000)
#
# 상황
#   공백도 포함한다.
#
# 구하는것
#   원본 문자열에서 찾는 문자열이 몇 개 나오는지
#   몇 번째 인덱스에서 나오는지
#
# 풀이
#   KMP 알고리즘을 이용하면 풀 수 있다.
#

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

T = list(input().split('\n')[0])
P = list(input().split('\n')[0])

lenT = len(T)
lenP = len(P)

F = [0 for i in range(lenP)]


def makeF():
  global lenP
  i = 0
  j = 1
  F[0] = 0
  
  while j < lenP:
    if P[i] == P[j]:
      F[j] = i + 1
      i += 1
      j += 1
    else:
      if i > 0:
        i = F[i - 1]
      else:
        F[j] = 0
        j += 1
        
makeF()

cnt = 0
resultArr = deque()

t = 0
p = 0

for t in range(lenT):
  while p > 0 and T[t] != P[p]:
    p = F[p - 1]
  if T[t] == P[p]:
    if p == lenP - 1:
      cnt += 1
      resultArr.append(t - p + 1)
      p = F[p]
    else:
      p += 1 
  
print(cnt)
while len(resultArr) > 0:
  output("%d " % resultArr.popleft())
