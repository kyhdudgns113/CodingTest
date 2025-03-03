# N : 정찰한 로봇의 수 (N <= 1,000)
# inp : K word1 word2 word3 ... wordK 로 이루어진 입력
#         K 는 숫자, word1~K 는 길이 15 이하의 알파벳 대문자로 이루어진 단어이다.
#         K <= 15
#
# 싱황
#   각 방이 트리 구조인 개미굴을 탐사한다.
#   각 방마다 음식이 담겨있다.
#   트리의 깊이가 더 깊어지는 방향으로만 탐사한다.
#   탐사하면서 만나는 음식을 기록한다.
#
# 구하는것
#   개미굴의 구조를 출력한다.
#     방마다 담겨있는 음식을 한 줄씩 출력한다.
#     부모 노드를 먼저 출력한다.
#     깊이가 같으면 알파벳 순으로 출력한다.
#     깊이가 1씩 내려갈때마다 "--" 를 왼쪽에 추가해서 출력한다.
#
#   입력예
#     3
#     2 B A
#     4 A B C D
#     2 A C
#   출력
#     A
#     --B
#     ----C
#     ------D
#     --C
#     B
#     --A
#
# 풀이
#   dictionary 자료구조를 이용하여 트리를 구성한다.
#   이후 재귀함수로 출력한다.
#
# 연산량
#   트리 원소의 최대 갯수는 N*K = 15,000 개이다.
#   이 원소들을 트리에 삽입하고 검색하는 연산을 하게 된다
#     = O(NK log NK)
#     = 약 수십만번
#     

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

trees = {}

def recurse(node, val, depth):
  output("--" * depth)
  output("%s\n" % val)
  
  childs = list(node.keys())
  if len(childs) > 0:
    childs.sort()
    for child in childs:
      recurse(node[child], child, depth + 1)

for nn in range(N):
  inp = list(input().strip().split())
  inp = inp[1::]
  
  nowNode = trees
  
  for now in inp:
    if now not in nowNode:
      nowNode[now] = {}
    nowNode = nowNode[now]
    
childs = list(trees.keys())
childs.sort()

for child in childs:
  recurse(trees[child], child, 0)
    