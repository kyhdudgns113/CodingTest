#
# cnts[n] : n 을 1로 만들기 위해 필요한 연산의 최소값
#  = min(cnts[n/3], cnts[n/2], cnts[n - 1])
#

import sys

input = sys.stdin.readline

n = int(input())

cnts = [0 for i in range(1000001)]
cnts[1] = 0
cnts[2] = 1
cnts[3] = 1

for i in range(4, 1000001):
  cnts[i] = i
  if i % 3 == 0:
    cnts[i] = min(cnts[i], cnts[i // 3] + 1)
  if i % 2 == 0:
    cnts[i] = min(cnts[i], cnts[i // 2] + 1)
  cnts[i] = min(cnts[i], cnts[i - 1] + 1)
  
print(cnts[n])