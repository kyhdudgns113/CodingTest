# 가로가 1 인 n 개의 직사각형이 일렬로 두고 이를 히스토그램이라 한다.
# 히스토그램에서 가장 넓이가 큰 직사각형을 찾는 문제다.
#
# n : 히스토그램의 가로 길이
# h[] : 히스토그램을 구성하는 직사각형들의 길이 배열
#
# 구하는것 : 직사각형 넓이의 최대값
#
# 풀이 O(n)
#   보통은 분할정복으로 푸는줄로 알골있다.
#   stack 을 이용하면 O(n) 으로 풀 수 있다.
#
#   stack[0] = {height: -1, idx: -1}
#   0 <= i < n
#     각 h[i] 에 대하여
#       topElem : stack 의 마지막 원소
#       nextElem : stack 의 마지막에서 2번째 원소소
#
#       Case 1. h[i] > topElem.height
#         - stack 에 그대로 넣는다.
#
#       Case 2. h[i] == topElem.height
#         - stack 맨 위 요소를 pop 한다.
#         - stack 에 {height: h[i], idx: i} 를 넣는다.
#
#       Case 3. h[i] < topElem.height
#         - 높이가 topElem.Height 인 직사각형의 크기를 구한다.
#         - 이 직사각형의 가로는
#           - nextElem.idx + 1 부터
#           - i - 1 까지이다.
#           - 가로길이는 (i - nextElem.idx - 1) 이다.
#         - 이 넓이의 최대값을 갱신한다.
#
#   남은 스택은
#   stack[i].height < stack[i + 1].height 이다.
#   스택의 뒤에서부터 해당 원소의 높이를 가지는 직사각형의 넓이를 구한다.
#
# 연산량은
#   처음에 스택에 넣기까지 : O(n)
#   스택에서 빼기까지 : O(n)
#   = O(n) 이다.         
# 분할정복의 O(n log n) 보다 빠르다.   

from collections import deque
import sys

input = sys.stdin.readline

while True:
  inp = list(map(int, input().split()))
  if inp[0] == 0:
    break
  n = inp[0]
  h = inp[1::]
  stack = deque()
  stack.append({'height': -1, 'idx': -1})
  maxArea = 0
  
  for i in range(0, n):
    nowHeight = h[i]
    nowIdx = i
    
    while len(stack) > 1:
      topElem = stack[-1]
      topHeight = topElem['height']
      topIdx = topElem['idx']
      
      if topHeight > nowHeight:
        startIdx = stack[-2]['idx']
        nowArea = topHeight * (nowIdx - startIdx - 1)
        maxArea = max(maxArea, nowArea)
        stack.pop()
      elif topHeight == nowHeight:
        stack.pop()
        break
      else:
        break
    # end while
    
    stack.append({'height': nowHeight, 'idx': nowIdx})
      
  # end for
  while len(stack) > 1:
    topElem = stack[-1]
    nextElem = stack[-2]
    height = topElem['height']
    idx = nextElem['idx']
    nowArea = height * (n - idx - 1)
    maxArea = max(maxArea, nowArea)
    stack.pop()
        
  
  print(maxArea)
  