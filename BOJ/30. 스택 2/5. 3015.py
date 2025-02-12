# n : 사람 수
# peoples[] : 사람 키(tall) 의 배열
#
# 상황
#   사람들이 일렬로 서 있다.
#   두 사람 A, B 사이에 있는 사람들 모두가 A, B 보다 키가 안 큰 경우, 1을 더한다.
#
# 구하는것
#   최종 결과
#
# 아이디어
#   i 번째 사람에 대하여
#     0 ~ (i - 1) 번째 사람들은 i 번째 사람보다 키가 작으면
#     i 번째 이후의 사람들이랑 마주칠 수 없다. (1을 더할 수 없다.)
#     == (i + 1)번쨰 사람부터는 0 ~ (i - 1) 번째 사람중
#         i 번째 사람보다 작은 사람은 고려할 필요가 없다.
#     == 0 ~ (i - 1) 번쨰 사람중 i 번째 사람보다 작은 사람은 전부 지운다.
#
# 풀이
#   stack 을 준비하며, {'people': peoples[i], 'cnt': 하단설명} 를 원소로 갖는다.
#     cnt : stack 에 남아있는 사람중, i 번째 사람보다 크거나 같은 사람들의 수
#
#   i 번째 사람에 대하여 스택 맨 위에 있는 원소를 last 라 하자.
#   Case 1. i 번째 사람이 last 보다 클 때
#     stack 을 pop 한다.
#     결과값을 1 늘린다.
#     이후 스택이 비어있으면 i 번째 사람을 추가한다.
#     last 를 갱신하여 조건들을 다시 확인한다.
#       - 이것 때문에 결과값을 1만 늘려도 된다.
#       - last 와 키가 같은 요소들을 전부 확인하게 된다.
#   Case 2. 둘이 키가 같을때
#     결과값을 last 의 cnt + 1 만큼 늘린다.
#       i 번째 사람이랑 만나는 이전 사람들의 경우의 수를 더하는것이다.
#       = last 랑 크거나 같은 사람들과 만나는 경우 + last 와 만나는 경우
#     stack 에 {'people': peoples[i], cnt: last.cnt + 1} 을 넣는다.
#       = cnt 는 해당 사람보다 크거나 같은 사람들의 수다
#       = last 보다는 한 명 더 많기 때문이다.
#     더 깉은곳으로 갈 필요는 없으므로 break 한다.
#   Case 3. last 가 더 클 때
#     결과값만 1 늘린다.
#     stack 에 {'peoples': peoples[i], 'cnt': 1} 을 넣는다.
#     반복문을 탈출한다.
#
# 해설
#   Case 1.
#     stack 에 있는 사람중 i 번째보다 작은 사람들과 만나는 경우를 전부 더해야 한다.
#     한 번에 한 사람씩만 계산하면 된다.
#     stack 에 있는 사람이 i 번째보다 작으면 stack 에 있을 필요가 없어진다.
#       - pop 한다.
#     만약 pop 하고서 stack 에 원소가 없으면 다음 횟수에 반복문을 탈출하게 된다.
#     이걸 방지하기 위해 pop 이후 스택이 비면 i 번째 사람을 스택에 넣어준다.
#
#   Case 2.
#     스택에 남아있는 모든 사람들은 i 번째보다 크거나 같다.
#     i 번째랑 만나는 경우는 스택에 남아있는 원소의 크기와 같다.
#       해설을 적고나니 cnt 를 굳이 더 넣어줄 필요가 없음을 깨달았다.
#
#   Case 3.
#     스택에 남아있는 나머지 원소들이랑 만날일은 없다.
#     결과값은 1 만 더해줘도 된다.

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
peoples = list(int(input()) for i in range(n))

stack = deque()

result = 0

for i in range(n):
  if i == 0:
    stack.append({'people': peoples[i], 'cnt': 0})
    continue
  
  while len(stack) > 0:
    last = stack[-1]
    
    if last['people'] < peoples[i]:
      stack.pop()
      result += 1
      if len(stack) == 0:
        stack.append({'people': peoples[i], 'cnt': 0})
        break
    elif last['people'] == peoples[i]:
      result += last['cnt'] + 1
      stack.append({'people': peoples[i], 'cnt': last['cnt'] + 1})
      break
    else:
      result += 1
      stack.append({'people': peoples[i], 'cnt': 1})
      break

print(result)