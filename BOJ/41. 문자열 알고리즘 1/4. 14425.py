#
# N : 사전에 있는 문자열의 갯수
# M : 검색할 문자열의 갯수
# S[] : 사전에 있는 문자열들
# inp[] : 찾을 문자열들
#
# 구하는것
#   찾는 문자열들 중에서 사전에 들어있는 갯수
#
# 풀이
#   사전에 문자열을 트리 형태로(dictionary)넣는다.
#

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = {}
for nn in range(N):
  inp = input().strip()
  S[inp] = 1
  
result = 0
for mm in range(M):
  inp = input().strip()
  if inp in S:
    result += 1
    
print(result)