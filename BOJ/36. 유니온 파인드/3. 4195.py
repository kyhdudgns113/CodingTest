# T : 테스트 케이스 수
# F : 친구 관계의 수(F <= 100,000)
# inp[] : (사람 A, 사람 B) 로 이루어진 배열 (F 개개)
#
# 상황
#   inp 로 들어온 사람들과 그들의 친구들은 서로 하나의 그룹이 되어 친구가 된다.
#
# 구하는것
#   inp 가 들어올 때마다 이 그룹의 인원수를 출력한다.
#
# 풀이
#   사람 A, 사람 B 가 입력으로 들어온다.
#   새로운 사람이면 각각에 새로운 그룹번호를 부여한다.
#   그리고 두 그룹을 union 을 이용하여 합친다.
#     합칠때 인원수도 더해준다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

# groupIdx 의 루트를 찾는 함수수
def findRoot(parentGroup, groupIdx):
  if groupIdx == parentGroup[groupIdx]:
    return groupIdx
  
  parentGroup[groupIdx] = findRoot(parentGroup, parentGroup[groupIdx])
  return parentGroup[groupIdx]

# 그룹 a 와 그룹 b 를 합치는 함수
# 합치면서 인원수도 합쳐준다.
# 합친 인원수를 리턴한다.
def union(groupMembers, parentGroup, a, b):
  ra = findRoot(parentGroup, a)
  rb = findRoot(parentGroup, b)
  
  if ra == rb:
    return groupMembers[ra]
  
  # 두 그룹을 합칠때는 숫자가 낮은쪽으로 합친다.
  if ra > rb:
    groupMembers[rb] += groupMembers[ra]
    parentGroup[ra] = rb
    return groupMembers[rb]
  else:
    groupMembers[ra] += groupMembers[rb]
    parentGroup[rb] = ra
    return groupMembers[ra]
  
# 실제 함수
for testCase in range(T):
  F = int(input())
  
  # groupNumber[A] = A 가 속한 그룹의 번호
  groupNumber = {}
  
  # groupMembers[i] = i 번째 그룹에 속한 멤버의 수
  # F 개의 입력마다 사람이 2명씩 추가될 수 있으므로
  # 배열의 크기를 2F 보다 크게 한다.
  groupMembers = [1 for i in range(2*F + 2)]
  
  # 새로 생성할 그룹의 번호
  # 생성할때마다 1 늘려준다,
  newGroupIdx = 0
  
  # parentGroup[a] : 그룹 a 의 부모그룹의 인덱스스
  parentGroup = [i for i in range(2*F + 2)]
  
  for ff in range(F):
    A, B = input().strip().split()
    
    # A 와 B 가 새로운 사람이면 새로운 그룹을 만들어 부여한다.
    if A not in groupNumber:
      groupNumber[A] = newGroupIdx
      newGroupIdx += 1
    if B not in groupNumber:
      groupNumber[B] = newGroupIdx
      newGroupIdx += 1
      
    # A 와 B 가 속한 그룹의 번호를 얻는다.
    ga = groupNumber[A]
    gb = groupNumber[B]
    
    # 두 그룹을 합치고 그 인원을 출력한다.
    output("%d\n" % union(groupMembers, parentGroup, ga, gb))
  
  
  
  