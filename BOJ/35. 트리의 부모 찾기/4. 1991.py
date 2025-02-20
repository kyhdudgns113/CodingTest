#
# n : 이진 트리의 원소 갯수
# inp[] : (부모, 왼쪽자식, 오른쪽자식) 의 배열. 알파벳 대문자나 . 으로만 들어온다.
#
# 상황
#   A 가 루트노드이다.
#
# 구하는것
#   VLR 출력
#   LVR 출력
#   LRV 출력한다.
#
# 풀이
#   각각 구하면 된다.
#

import sys

input = sys.stdin.readline


n = int(input())
childs = [[-1, -1] for i in range(26)]
parents = [0 for i in range(27)]

def charIdx(c):
  if ord("A") <= ord(c) <= ord("Z"):
    return ord(c) - ord("A")
  else:
    return -1

def getChar(idx):
  if idx != -1:
    return chr(ord("A") + idx)
  else:
    return ""
  
def lvr(nowIdx):
  if nowIdx == -1:
    return ""
  
  left = childs[nowIdx][0]
  right = childs[nowIdx][1]
  
  return lvr(left) + getChar(nowIdx) + lvr(right)

def vlr(nowIdx):
  if nowIdx == -1:
    return ""
  
  left = childs[nowIdx][0]
  right = childs[nowIdx][1]
  
  return getChar(nowIdx) + vlr(left) + vlr(right)

def lrv(nowIdx):
  if nowIdx == -1:
    return ""
  
  left = childs[nowIdx][0]
  right = childs[nowIdx][1]
  
  return lrv(left) + lrv(right) + getChar(nowIdx)

for i in range(n):
  parent, left, right = map(str, input().strip().split())
  pIdx = charIdx(parent)
  leftIdx = charIdx(left)
  rightIdx = charIdx(right)
  
  childs[pIdx] = [leftIdx, rightIdx]
  parents[leftIdx] = pIdx
  parents[rightIdx] = pIdx
  
print(vlr(0))
print(lvr(0))
print(lrv(0))
