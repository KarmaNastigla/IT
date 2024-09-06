import math
def cos_dist (arr1, arr2):

    if len(arr1) != len(arr2):
        raise ValueError("Векторы должны быть одной длинны.")

    numerator = sum(x * y for x, y in zip(arr1, arr2))
    denominator1 = math.sqrt(sum(x**2 for x in arr1))
    denominator2 = math.sqrt(sum(y**2 for y in arr2))
    res = numerator / (denominator1 * denominator2)
    return res

arr1 = [float(i) for i in input().split()]
arr2 = [float(i) for i in input().split()]

try:
    cosine_distance = cos_dist(arr1, arr2)
except ValueError as e:
    print(e)
else:
    print(cosine_distance)