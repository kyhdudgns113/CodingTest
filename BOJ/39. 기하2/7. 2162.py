import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

N = int(input())

lines = [list(map(int, input().split())) for i in range(N)]

groupNumber = [i for i in range(N + 1)]
membersArr = [1 for i in range(N + 1)]

def findRoot(now):
  if groupNumber[now] == now:
    return now
  
  groupNumber[now] = findRoot(groupNumber[now])
  
  return groupNumber[now]

def union(a, b):
  ra = findRoot(a)
  rb = findRoot(b)
  
  if ra == rb:
    return
  
  if ra > rb:
    groupNumber[ra] = rb
    membersArr[rb] += membersArr[ra]
  else:
    groupNumber[rb] = ra
    membersArr[ra] += membersArr[rb]
    
def getArea(x0, y0, xm, ym, xz, yz):
  area1 = (xm - x0) * (ym + y0)
  area2 = (xz - xm) * (yz + ym)
  area3 = (x0 - xz) * (y0 + yz)
  
  return area1 + area2 + area3

def isCross(a, b):
  x1, y1, x2, y2 = lines[a]
  x3, y3, x4, y4 = lines[b]
  
  area132 = getArea(x1, y1, x3, y3, x2, y2)
  area142 = getArea(x1, y1, x4, y4, x2, y2)
  area314 = getArea(x3, y3, x1, y1, x4, y4)
  area324 = getArea(x3, y3, x2, y2, x4, y4)
  
  cond1 = False
  cond2 = False
  
  if area132 >= 0 and area142 <= 0 or area132 <= 0 and area142 >= 0:
    cond1 = True
  if area314 >= 0 and area324 <= 0 or area314 <= 0 and area324 >= 0:
    cond2 = True
    
  xx1, xx2 = min(x1, x2), max(x1, x2)
  xx3, xx4 = min(x3, x4), max(x3, x4)
  
  yy1, yy2 = min(y1, y2), max(y1, y2)
  yy3, yy4 = min(y3, y4), max(y3, y4)
  
  if area132 == 0 and area142 == 0 and area314 == 0 and area324 == 0:
    if xx1 < xx2 < xx3 < xx4 or xx3 < xx4 < xx1 < xx2:
      cond1 = False
    if yy1 < yy2 < yy3 < yy4 or yy3 < yy4 < yy1 < yy2:
      cond2 = False
    
  return cond1 & cond2

for i in range(N):
  for j in range(i + 1, N):
    if isCross(i, j):
      union(i, j)
  
groupList = []

for i in range(N):
  ri = findRoot(i)
  
  if ri not in groupList:
    groupList.append(ri)

maxMembers = 0

for group in groupList:
  rg = findRoot(group)
  
  if maxMembers < membersArr[rg]:
    maxMembers = membersArr[rg]
    
print(len(groupList))
print(maxMembers)


