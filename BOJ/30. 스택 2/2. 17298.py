# n : 수열의 원소 갯수
# a[] : 수열
#
# 구하는것
#   0 <= i < n 에 대하여
#   a[i] 이후의 a[i] 보다 큰 수 중에서 인덱스가 i 랑 가장 가까운 수
#     없으면 -1
#
# 풀이
#   stack[]
#     {val: a[i], idx: i} 들이 저장되어 있다.
#   nge[i]
#     a[i] 뒤에 있는 수 중 a[i] 보다 크면서 a[i] 와 가장 가가운곳에 있는 수
#     초기값은 -1 로 한다.
#
#   0 <= i < n 에 대하여
#     스택 크기가 1 이상일때 다음을 반복한다.
#       elem : 스택의 마지막 요소
#         Case 1. elem.val 이 a[i] 보다 작을때
#           nge[elem.idx] = a[i] 이다.
#           스택을 pop 한다.
#         Case 2. elem.val 이 a[i] 보다 작지는 않을때
#           스택의 나머지 요소들은 전부 a[i] 보다 작지 않다.
#           스택과 관련된 반복문을 탈출한다.
#     {val: a[i], idx: i} 를 스택에 넣는다.
#
# 연산량
#   - 모든 수열의 원소에 대하여
#   - 해당 원소는 최대 2개의 연산에만 관여한다.
#     1. 스택에 넣기
#     2. 스택에서 빼기(안 할수도 있다)
#   = O(n) = 1,000,000
#     

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))

nge = [-1 for i in range(n)]

stack = deque()

for i in range(n):
  while len(stack) > 0:
    elem = stack[-1]
    if elem['val'] < a[i]:
      nge[elem['idx']] = a[i]
      stack.pop()
    else:
      break
  stack.append({'val': a[i], 'idx': i})
  
for i in range(n):
  output(str(nge[i]) + ' ')

