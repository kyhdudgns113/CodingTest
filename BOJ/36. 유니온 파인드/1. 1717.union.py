#
# 1717 문제를 union 을 이용하여 풀었다. 속도 향상을 위해서다.
#
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int,input().split())

parent = [0] * (n+1) # 부모 테이블 생성
for i in range(n+1): # 자기 자신을 부모로 설정
  parent[i] = i

# 루트 노드 찾는 함수
def find(a):
  if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
    return a
  p = find(parent[a]) # a의 루트 노드 찾기
  parent[a] = p # 부모 테이블 갱신
  return parent[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a,b):
  a = find(a) # a의 루트 노드 찾기
  b = find(b) # b의 루트 노드 찾기

  if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
    return
  if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
    parent[b] = a
  else:
    parent[a] = b

for _ in range(m):
  o, a, b = map(int,input().split()) # operation, 원소, 원소
  if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
    union(a,b)
  elif o == 1: # 두 원소가 동일한 집합인지 판단
    if find(a) == find(b):
      print('YES')
    else:
      print('NO')