# S : 입력 문자열
# bomb : 폭탄 문자열
#
# 상황
#   S 에서 폭탄 문자열들을 전부 없애고 합친다.
#   합치고 난 뒤에 다시 생기는 폭탄 문자열도 전부 없앤다.
#
# 구하는것
#   최종적으로 남는 문자열
#
# 풀이
#   stack 에 S 를 하나씩 넣으면서 bomb 이랑 얼마나 일치하는지 체크한다.
#   bomb 이랑 일치하면 stack 에서 bomb 만큼 날린다.

from collections import deque
import sys

input = sys.stdin.readline

S = list(input().strip())
bomb = list(input().strip())

stack = deque()

# bombIdx 를 찾는다.
# bombIdx : 다음번에 들어오는 입력이 일치해야 하는 폭탄 문자열에서의 인덱스
# 스택 끝부분이 bomb 이랑 일치하는 길이랑 같다.
def findBombIdx():
  for i in range(len(bomb)):
    lenBomb = len(bomb) - i
    if len(stack) < lenBomb:
      continue
    for j in range(lenBomb):
      if bomb[lenBomb - 1 - j] != stack[-1 - j]:
        break
      elif j == lenBomb - 1:
        return lenBomb
  return 0

bombIdx = 0
for s in S:
  stack.append(s)
  if s == bomb[bombIdx]:
    bombIdx += 1
  else:
    bombIdx = findBombIdx()
  while bombIdx == len(bomb):
    # stack 에서 bomb 만큼 빼기
    i = 0
    while i < len(bomb):
      stack.pop()
      i += 1      
    # stack 끝부분에서 bomb 이랑 얼마나 일치하는지 확인하기
    bombIdx = findBombIdx()

if len(stack) > 0:
  result = ''.join(stack)
  print(result)
else:
  print("FRULA")
    
    