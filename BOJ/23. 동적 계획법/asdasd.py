tempArr = [3*i for i in range(10)]
res = []

def binarySearch(val, l, r):
  c = (l + r) // 2
  if val == tempArr[c]:
    return c
  
  if l + 1 >= r:
    return r
  
  if val < tempArr[c]:
    return binarySearch(val, l, c)
  else:
    return binarySearch(val, c, r)
  
for i in range(30):
 res.append(binarySearch(i, 0, 9))

print(res)