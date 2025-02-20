#
# n : 임의의 수(n <= 1,000,000)
#
# 상황
#   n 이 3의 배수면 3을 나눌 수 있다.
#   n 이 2의 배수면 2를 나눌 수 있다.
#   n 에 1을 뺼 수 있다.
#
# 구하는것
#   1. n 을 1로 만드는 가장 빠른 횟수
#   2. n 을 1로 가장 빨리 만드는 경로
#
# 풀이
#   1 <= i <= 1,000,000 에 대하여 다음 연산 수행
#     i + 1, 2 * i, 3 * i 에 대하여
#       최소 연산수 갱신
#         i 의 연산수 + 1 을 넣는다.
#       최소 연산 갱신됬으면 i 도 저장    
#         next[i + 1] 이나 next[2 * i], next[3 * i] 에
#         i 를 넣는다.
#   minCnt[i] 를 출력한다.
#   next[i] 를 계속 출력한다.
#     next[i] 랑 next[next[i]] 가 같아질때까지 출력한다.
#       둘 다 1이 된다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
G = 1000001

cntAndNext = [[G, G] for i in range(G)]

cntAndNext[1] = [0, 1]

for i in range(1, G):
  nowCnt = cntAndNext[i][0]
  if i + 1 < G and cntAndNext[i + 1][0] > nowCnt:
    cntAndNext[i + 1] = [nowCnt + 1, i]
  if 2*i < G and cntAndNext[2*i][0] > nowCnt:
    cntAndNext[2 * i] = [nowCnt + 1, i]
  if 3*i < G and cntAndNext[3*i][0] > nowCnt:
    cntAndNext[3 * i] = [nowCnt + 1, i]
    
print(cntAndNext[n][0])
now = n
while True:
  output("%d " % now)
  next = cntAndNext[now][1]
  if now == next:
    break
  now = next
  
    