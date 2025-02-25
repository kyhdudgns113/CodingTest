#
# N : 도시의 개수
# M : 도시를 연결하는 간선의 갯수
# inp[] : (도시 A, 도시 B) 로 구성된 배열.
#
# 상황
#   간선을 최소한으로 사용한다.
#
# 구하는것
#   모든 도시를 연결하기 위한 간선의 최소 개수
#
# 풀이
#   N 개의 점을 연결하기 위해 필요한 가장 적은 간선은 N - 1 개이다.
#   이것보다 더 많이 필요한 경우는 없다.
#

import sys

input = sys.stdin.readline

T = int(input())

for testCase in range(T):
  N, M = map(int, input().split())
  
  connections = [[]]
  
  for mm in range(M):
    A, B = map(int, input().split())
  
  print(N - 1)
    
    
