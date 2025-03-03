#
# 아래 입력을 받을 수 없을때까지 받는다
#
# N : 단어의 수 (N <= 100,000)
# words[i] : N 개의 단어. 길이는 80 이하인 소문자로만 구성되어 있다.
#             - 단어 길이의 총합은 100만 이하하
#
# 상황
#   자판으로 단어를 입력한다.
#   단어의 첫 번째 글자는 무조건 입력해야 한다.
#   다음번째 글자까지의 경우가 하나라면 자동으로 입력된다.
#     주어진 단어가 hello, hell, hi 일때
#       h 와 e 를 입력하면 ll 이 자동으로 완성된다.
#
# 구하는것
#   모든 단어를 입력할때 평균적으로 누르는 자판의 갯수
#   소수점 2째자리까지 출력한다.
#   나머지는 반올림 한다.
#
# 풀이
#   단어 철자마다 트리 구조를 만들고 재귀함수로 풀 수 있다.
#     - 현재 노드의 자식이 1개밖에 없으면 클릭한 횟수를 유지한채로 재귀를 호출한다.
#     - 자식이 2개 이상이면 클릭한 횟수를 1 늘리고 재귀를 호출한다.
#
# 연산량
#   트리 원소 개수가 가장 많을때 = 100만 (주어지는 단어의 길이 총합이 100만으로 제한됨.)
#   모든 원소를 삽입 및 검색
#     = O(log 100만)
#     = 몇백~몇천   
#

import sys

input = sys.stdin.readline
output = sys.stdout.write

#
# nowNode 에서 타자를 쳐야하는 횟수 총합
# nowNode 까지 depth 만큼 넘어왔고 clicked 만큼 타자를 쳤다는 의미이다.
#
def recurse(nowNode, clicked, depth):
  if nowNode["CNT"] == 1:
    return clicked
  if nowNode["CNT"] == 0:
    return clicked - 1
  
  childs = list(nowNode.keys())
  newClicked = clicked
  
  # 첫 번째 철자를 입력할때는 자손에게 클릭수를 1 늘려서 주지 않는다.
  # 자손이 2개 이상 + CNT 1개 = 3개 이상이어야 클릭수가 1 더 는다.
  if depth > 0 and len(childs) > 2:
    newClicked += 1
  
  result = 0
  for child in childs:
    if child == "\n":
      result += clicked
    elif child != "CNT":
      ret = recurse(nowNode[child], newClicked, depth + 1)
      result += ret
      
  return result
  

while True:
  try:
    N = int(input())
    tree = {"CNT": 0}
    
    for nn in range(N):
      word = list(input())
      nowNode = tree
      for i in range(len(word)):
        c = word[i]
        if c not in nowNode:
          nowNode[c] = {"CNT": 0}
        nowNode["CNT"] += 1
        nowNode = nowNode[c]
    
    output("%.2f\n" % (recurse(tree, 1, 0) / N))
  except:
    break
