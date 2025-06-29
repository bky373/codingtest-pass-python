# 1 4  3 3
# 3 2  3 3
# 4 1

arr1 = [[1,4], [3,2], [4,1]]
arr2 = [[3,3], [3,3]]
# arr1 = [[1, 2], [3, 4]]
# arr2 = [[1, 1], [1, 1]]

def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    ret = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2): # c1 돌고, c2 돈다
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]
    return ret

print(solution(arr1, arr2))
