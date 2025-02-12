# n : 수열의 원소 갯수
# a[] : 수열
#
# 상황
#   f[i](코드에서는 cnts[]) : a[i] 가 a 에 등장한 횟수
#   ngf[i]
#     - i 번째 수보다 뒤에 있으면서
#     - i 번째 수보다 많이 등장한 수 중에서
#     - i 번째 수랑 가장 가까운곳에 위치한 수
#
# 구하는것
#   ngf[] 전부
#
# 풀이
#
#   1. f[] 를 구한다.
#     a[] 를 순회하면서 등장한 횟수를 더해준다 : O(n)

#   2. stack 을 만든다.
#     {val: a[i], idx: i} 들을 저장한다.

#   3. 0 <= i < n 에 대하여
#     a. 스택의 맨 위 원소 elem 이랑 비교한다.
#       Case 1. f[a[i]] > elem.val
#         - 현재 숫자의 등장횟수가 더 큰 경우
#         - elem.idx 번째 숫자의 ngf 는 a[i] 이다.
#         - 해당 원소를 없앤다.
#         - 만약 원소를 없애고 stack 이 비어있으면
#           = stack 에 {val: a[i], idx: i} 를 넣는다.
#           = 이후 a 를 빠져나온다.
#       Case 2. f[a[i]] == elem.val
#         - 현재 숫자의 등장횟수와 스택 최상단 등장횟수가 같은 경우
#         - elem 을 포함한 stack 에 남아있는 모든 원소들보다 등장횟수가 적다.
#         - 스택에 넣고 a 반복문을 빠져나온다.
#       Case 3. 
#         - 현재 숫자의 등장횟수가 더 작은 경우
#         - stack 에 있는 나머지 숫자들도 현재 숫자보단 등장을 적게 하진 않는다.
#         - 스택에 넣고 a 반복문을 빠져나온다.
#   

from collections import deque
import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))

cnts = [0 for i in range(1000001)]

for aa in a:
  cnts[aa] += 1
  
ngf = [-1 for i in range(n)]
stack = deque()


for i in range(n):
  if i == 0:
    stack.append({'val': cnts[a[i]], 'idx': i})
    continue
  
  while len(stack) > 0:
    elem = stack[-1]
    
    if elem['val'] < cnts[a[i]]:
      ngf[elem['idx']] = a[i]
      stack.pop()
      if len(stack) == 0:
        stack.append({'val': cnts[a[i]], 'idx': i})
        break
    elif elem['val'] == cnts[a[i]]:
      stack.append({'val': cnts[a[i]], 'idx': i})
      break
    else:
      stack.append({'val': cnts[a[i]], 'idx': i})
      break
    
for num in ngf:
  output(str(num) + ' ')
      

      