# n : 입력의 개수
# 입력 > 0 : 배열에 넣는다.
# 입력 = 0 : 배열에서 가장 작은 원소를 pop 하고 출력
#
# 풀이
#   우선순위 큐를 구현하면 된다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

pq = []

def pushPQ(val):
  pq.append(val)
  nowIdx = len(pq) - 1
  while nowIdx > 0:
    sonIdx = (nowIdx - 1) // 2
    if pq[sonIdx] > pq[nowIdx]:
      pq[sonIdx], pq[nowIdx] = pq[nowIdx], pq[sonIdx]
      nowIdx = sonIdx
    else:
      break

def popPQ():
  if len(pq) == 0:
    return "0\n"
  result = pq[0]
  pq[0] = pq[-1]
  pq.pop()
  nowIdx = 0
  while nowIdx < len(pq):
    if 2 * nowIdx + 1 >= len(pq):
      break
    elif 2 * nowIdx + 2 >= len(pq):
      if pq[nowIdx] > pq[2*nowIdx + 1]:
        pq[nowIdx], pq[2*nowIdx + 1] = pq[2*nowIdx + 1], pq[nowIdx]
        nowIdx = 2*nowIdx + 1
      else:
        break
    else:
      if pq[2*nowIdx + 1] > pq[2*nowIdx + 2] and pq[nowIdx] > pq[2*nowIdx + 2]:
        pq[nowIdx], pq[2*nowIdx + 2] = pq[2*nowIdx + 2], pq[nowIdx]
        nowIdx = 2*nowIdx + 2
      elif pq[2*nowIdx + 1] <= pq[2*nowIdx + 2] and pq[nowIdx] > pq[2*nowIdx + 1]:
        pq[nowIdx], pq[2*nowIdx + 1] = pq[2*nowIdx + 1], pq[nowIdx]
        nowIdx = 2*nowIdx + 1
      else:
        break
  return str(result) + '\n'

for _ in range(n):
  inp = int(input())
  
  if inp == 0:
    output(popPQ())
  else:
    pushPQ(inp)
