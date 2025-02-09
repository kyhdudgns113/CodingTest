# n : 입력의 개수
# 입력 > 0 : 배열에 넣는다.
# 입력 = 0 : 배열에서 가장 절대값이 작은 원소를 pop 하고 출력
#           - 절대값이 같으면 더 작은 원소를 선택
#
# 풀이
#   우선순위 큐를 구현하면 된다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())

pq = []

def aLessThenB(a, b):
  if abs(a) < abs(b) or abs(a) == abs(b) and a <= b:
    return True
  return False

def pushPQ(val):
  pq.append(val)
  nowIdx = len(pq) - 1
  while nowIdx > 0:
    nextIdx = (nowIdx - 1) // 2
    v0 = pq[nowIdx]
    v1 = pq[nextIdx]
    if aLessThenB(v0, v1):
      pq[nowIdx], pq[nextIdx] = v1, v0
    nowIdx = nextIdx
      
def popPQ():
  if len(pq) == 0:
    return "0\n"
  
  result = pq[0]
  pq[0] = pq[-1]
  pq.pop()
  nowIdx = 0
  while nowIdx < len(pq):
    if 2*nowIdx + 1 >= len(pq):
      break
    elif 2*nowIdx + 2 >= len(pq):
      if aLessThenB(pq[2*nowIdx + 1], pq[nowIdx]):
        pq[nowIdx], pq[2*nowIdx + 1] = pq[2*nowIdx + 1], pq[nowIdx]
        nowIdx = 2*nowIdx + 1
      else:
        break
    else:
      if aLessThenB(pq[2*nowIdx + 1], pq[nowIdx]) and aLessThenB(pq[2*nowIdx + 1], pq[2*nowIdx + 2]):
        pq[nowIdx], pq[2*nowIdx + 1] = pq[2*nowIdx + 1], pq[nowIdx]
        nowIdx = 2*nowIdx + 1
      elif aLessThenB(pq[2*nowIdx + 2], pq[nowIdx]) and aLessThenB(pq[2*nowIdx + 2], pq[2*nowIdx + 1]):
        pq[nowIdx], pq[2*nowIdx + 2] = pq[2*nowIdx + 2], pq[nowIdx]
        nowIdx = 2*nowIdx + 2
      else:
        break
  return str(result) + '\n'

for _ in range(n):
  inp = int(input())
  
  if inp == 0:
    output(popPQ())
  else:
    pushPQ(inp)