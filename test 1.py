def unic(arr):
    res = []
    for i in arr:
       if i not in res:
           res.append(i)
    return sorted(res)

arr = [1, 8, 2, 3, 4, 2, 5, 1, 6, 3]
print(*unic(arr))