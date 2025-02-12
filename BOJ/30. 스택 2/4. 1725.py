# 히스토그램에서 가장 큰 직사각형 넓이 구하는 문제이다.
# 26. 분할정복 -> 9. 6549.py 랑 풀이가 동일하다.
# 

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
heights = list(int(input()) for i in range(n))

stack = deque()
stack.append({'height': -1, 'idx': -1})
maxArea = -1

for i in range(n):
  if i == 0:
    stack.append({'height': heights[i], 'idx': i})
    continue
  
  while len(stack) > 1:
    elem = stack[-1]
    prev = stack[-2]
    
    if elem['height'] > heights[i]:
      width = i - prev['idx'] - 1
      nowArea = elem['height'] * width
      maxArea = max(maxArea, nowArea)
      stack.pop()
      if len(stack) == 1:
        stack.append({'height': heights[i], 'idx': i})
        break
    elif elem['height'] == heights[i]:
      stack.pop()
      stack.append({'height': heights[i], 'idx': i})
      break
    else:
      stack.append({'height': heights[i], 'idx': i})
      break

while len(stack) > 1:
  elem = stack.pop()
  width = n - 1 - stack[-1]['idx']
  nowArea = width * elem['height']
  maxArea = max(maxArea, nowArea)

print(maxArea)
  