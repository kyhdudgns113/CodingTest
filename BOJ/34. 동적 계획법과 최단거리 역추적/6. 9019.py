#
# t : 테스트 케이스
# a : 시작 숫자 (4자리)
# b : 목표 숫자 (4자리리)
#
# 상황
#   하나의 숫자에 대해서 다음 연산 중 하나를 수행할 수 있다.
#   D : 숫자에 2를 곱하고 10,000 을 나눈 나머지를 구한다.
#   S : 1을 뺀다. 0에서 1 빼면 9999로 만든다.
#   L : 숫자를 왼쪽으로 민다. 1234 는 2341 이 된다.
#   R : 숫자를 오른쪽으로 민다. 1234 는 4123 이 된다.
#
# 구하는것
#   a 에서 b 가 되기까지 최단경로를 출력한다.
#     1234 에서 3412 가 될 때는
#       1234 -> L -> 2341
#       2341 -> L -> 3412 이므로
#       먼저 선택한 알파벳 순서로 LL 을 출력한다.
#
# 풀이
#   bfs 로 풀면 된다.
#   prevInfo 에 해당 숫자를 만들기 전에 무슨 숫자에서 무슨 연산을 했는지 기록한다.
#

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

t = int(input())

for tt in range(t):
  a, b = map(int, input().split())
  
  prevInfo = [[-1, ""] for i in range(20002)]
  
  nextVisit = deque()
  nextVisit.append(a)
  prevInfo[a][0] = a
  
  while len(nextVisit) > 0:
    now = nextVisit.popleft()
    
    if now == b:
      break
    
    D = (2 * now) % 10000
    if prevInfo[D][0] == -1:
      prevInfo[D] = [now, "D"]
      nextVisit.append(D)
      
      if D == b:
        break
    
    S = (now + 9999) % 10000
    if prevInfo[S][0] == -1:
      prevInfo[S] = [now, "S"]
      nextVisit.append(S)
      
      if S == b:
        break
      
    L = (10*now + now // 1000) % 10000
    if prevInfo[L][0] == -1:
      prevInfo[L] = [now, "L"]
      nextVisit.append(L)
      
      if L == b:
        break
    
    R = (now // 10 + 1000 *(now % 10))
    if prevInfo[R][0] == -1:
      prevInfo[R] = [now, "R"]
      nextVisit.append(R)
      
      if R == b:
        break
  # end while    

  result = []
  now = b
  while True:
    result.append(prevInfo[now][1])
    if now == a:
      break
    now = prevInfo[now][0]
    
  lenResult = len(result)
  for i in range(lenResult):
    output(result[lenResult - 1 - i])
    
  output("\n")
  
  
  