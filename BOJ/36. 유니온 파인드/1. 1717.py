#
# n : 서로 다른 숫자의 갯수
# m : 명령어 갯수
#
# input = [명령, a, b] 로 구성된 m 개의 배열
#
# 구하는것
#   처음엔 모든 숫자가 각각의 집합에 속해있다.
#   명령 == 0 이면 a와 b 가 속한 집합을 하나로 합친다.
#   명령 == 1 이면 a 와 b 가 같은 집합에 속하는지 여부를 출력한다.
#
# 풀이
#   두 집합의 배열을 그대로 더했다.
#   

import sys

input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

whichTeam = [i for i in range(n + 1)]
members = [[i] for i in range(n + 1)]

def combine(a, b):
  aTeam = whichTeam[a]
  bTeam = whichTeam[b]
  
  if aTeam == bTeam:
    return
  
  baseTeam = bTeam
  otherTeam = aTeam
  
  if len(members[aTeam]) > len(members[bTeam]):
    baseTeam = aTeam
    otherTeam = bTeam
    
  
  for member in members[otherTeam]:
    whichTeam[member] = baseTeam
  
  members[baseTeam] = members[baseTeam] + members[otherTeam]    
  members[otherTeam] = []

for mm in range(m):
  order, a, b = map(int, input().split())
  
  if order == 0:
    combine(a, b)
  else:
    if whichTeam[a] == whichTeam[b]:
      output("YES\n")
    else:
      output("NO\n")

