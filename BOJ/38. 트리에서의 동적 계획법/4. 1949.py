# N : 마을의 갯수 (N <= 10,000)
# peiples[] : 각 마을의 인구수
# inp[] : (A, B) 로 이루어진 배열. 마을 A 와 B 가 직접 연결되었다는 의미이다.
#   배열의 원소는 N - 1 개다.
#
# 상황
#   모든 마을간의 연결은 트리 구조를 이룬다.
#   마을 중에서 우수 마을을 선정할 수 있다.
#     - 우수 마을 옆에는 우수 마을을 선정할 수 없다.
#     - 우수마을이 아닌 마을은 우수마을과 꼭 연결이 되어있어야 한다.
#
# 구하는것
#   가장 많은 우수마을 인구수수
#
# 풀이
#   루트노드를 임의로 선정한다.
#   다음 3개의 함수를 재귀적으로 호출한다.
#     1. 나를포함(now)
#       - now 를 루트노드로 한다.
#       - now 를 우수마을로 할 때, 최대 인원수를 리턴한다.
#       - now 의 자식들은 전부 우수마을이 아니어야 한다.
#
#     2. 나를 제외, 자식중 하나 이상은 무조건 포함
#       - now 를 루트노드로 한다.
#       - now 를 우수마을로 안하고, 자식중 하나 이상은 우수마을이다.
#       - 하나 이상의 자식을 우수마을로 선정해야 한다.
#
#     3. 나를 제외, 자식들도 전부 제외
#       - 나의 부모가 우수마을이고, 나의 자식들이 전부 우수마을인 자식이 하나 이상 있으면 된다.
#       - 모든 자식들은 우수마을이 아니어야 하고, 그들이 자식중 하나 이상은 우수마을이어야 한다.
#         == 모든 자식은 2번째 함수여야 한다.
#
#   함수에 대한 자세한 설명은 코드에 주석으로 달아놨다.
#
# 연산량
#   최악의 경우에도 각 마을은 상수번 연산된다.
#     - 나의 부모 마을에서 연산이 3번 되고 끝이다.
#     = O(N)
#   
import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

N = int(input())

peoples = list(map(int, input().split()))

connections = [[] for i in range(N + 1)]

for nn in range(N - 1):
  A, B = map(int, input().split())
  connections[A].append(B)
  connections[B].append(A)
  
includeMeArr = [None for i in range(N + 1)]
excludeMeArr = [None for i in range(N + 1)]
excludeBothArr = [None for i in range(N + 1)]

#
# now 가 루트노드이며, now 가 우수마을일때 최대 인원
#
def includeMe(now, parent):
  if includeMeArr[now] != None:
    return includeMeArr[now]
  
  result = peoples[now - 1]
  
  #
  # now 가 우수마을이면 자식은 무조건 우수마을이 아니어야 한다.
  #
  for child in connections[now]:
    if child != parent:
      result += max(
        excludeMe(child, now),
        excludeBoth(child, now) 
      )
      
  includeMeArr[now] = result
 
  return result

#
# now 가 루트노드이며, now 가 우수마을이 아니며
# 자식중 하나 이상이 우수마을일때 최대 인원
#
def excludeMe(now, parent):
  if excludeMeArr[now] != None:
    return excludeMeArr[now]
  
  result = 0
  incChild = []
  excChild = []
  
  # child 가 포함된 경우와 포함되지 않은 경우의 인원을 구한다.
  for child in connections[now]:
    if child != parent:
      incChild.append(includeMe(child, now))
      excChild.append(max(
        excludeMe(child, now),
        excludeBoth(child, now)
      ))
  
  # child 중에서 어느 마을을 우수마을로 선정해야 하는지 고른다.
  # child 가 우수마을일때와 그렇지 않을때의 차이가 가장 큰 것을 고른다.
  #   - 인원수를 최대로 해야 하기 때문이다.
  # 가장 차이가 큰 마을을 pivotIdx 로 한다.
  pivotIdx = 0
  tempMax = - (10 ** 9)
  lenChilds = len(incChild)
  
  for i in range(lenChilds):
    diff = incChild[i] - excChild[i]
    if tempMax < diff:
      tempMax = diff
      pivotIdx = i
  
  #
  # pivotIdx 가 아닌 경우는 child 가 우수마을인 경우(incChild) 와 우수마을이 아닌경우(excChild)
  # 중에서 최대값을 더한다.
  # pivotIdx 인 경우는 무조건 우수마을이어야 하므로 incChild 를 더한다.
  #
  for i in range(lenChilds):
    if i != pivotIdx:
      result += max(incChild[i], excChild[i])
    else:
      result += incChild[i]
    
  excludeMeArr[now] = result
  return result

#
# now 가 루트노드이며, now 가 우수마을이 아니며
# 모든 자식들이 우수마을이 아닐때의 최대 인원
#
def excludeBoth(now, parent):
  if excludeBothArr[now] != None:
    return excludeBothArr[now]
  
  result = 0
  
  # child 가 전부
  #   - 본인은 우수마을이 아니고
  #   - child 의 자식 중 하나는 우수마을
  #   이어야 한다.
  # excludeMe(child) 의 값이 0 이면 child 가 우수마을이 아닌 경우는 없어야 한다는 것이다.
  # 그때는 excludeBoth(now) 값을 절대로 쓰지 못하게 제일 작은 수를 넣는다.
  for child in connections[now]:
    if child != parent:
      excChild = excludeMe(child, now)
      if excChild == 0:
        result += - (10 ** 9)
      else:
        result += excChild      
  
  excludeBothArr[now] = result
  return result

print(max(includeMe(1, 1), excludeMe(1, 1)))
