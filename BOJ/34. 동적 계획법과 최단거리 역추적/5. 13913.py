# pypy 로 돌렸다.
#
# n : 시작숫자
# k : 끝 숫자
#
# 상황
#   n 에서 시작한다
#   1을 더할수도, 뺄 수도, 2를 곱할수도 있다.
#
# 구하는것
#   가장 빠르게 k 를 만드는 연산수
#   그 때 n 에서 k 까지 변하는 과정
#
# 풀이
#   bfs 로 풀면 된다.
#   연산수를 갱신할때 히스토리를 남기도록 한다.

from collections import deque

import sys

input = sys.stdin.readline
output = sys.stdout.write

n, k = map(int, input().split())

cnts = [10 ** 6 for i in range(200002)]
prev = [-1 for i in range(200002)]

nextVisit = deque()
nextVisit.append(n)
cnts[n] = 0

while len(nextVisit) > 0:
  now = nextVisit.popleft()
  
  if 2 * now <= 200000 and cnts[2 * now] == 10 ** 6:
    cnts[2 * now] = cnts[now] + 1
    prev[2 * now] = now
    nextVisit.append(2 * now)
  if now > 0 and cnts[now - 1] == 10 ** 6:
    cnts[now - 1] = cnts[now] + 1
    prev[now - 1] = now
    nextVisit.append(now - 1)
  if now <= 200000 and cnts[now + 1] == 10 ** 6:
    cnts[now + 1] = cnts[now] + 1
    prev[now + 1] = now
    nextVisit.append(now + 1)
    
print(cnts[k])

arrLen = cnts[k]
now = k

# pypy 에서 메모리 초과가 뜨길래 cnts 배열을 재활용했다.
for i in range(1, arrLen + 1):
  cnts[arrLen + 1 - i] = now
  now = prev[now]
cnts[0] = n

for i in range(arrLen + 1):
  output("%d " % cnts[i])
    