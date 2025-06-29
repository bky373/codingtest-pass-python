arr1 = [[1,4], [3,2], [4,1]]
arr2 = [[3,3], [3,3]]
# arr1 = [[1, 2], [3, 4]]
# arr2 = [[1, 1], [1, 1]]
arr3 = [[0 for _ in range(len(arr2))] for _ in range(len(arr1))]


def solution(arr1, arr2):
    for k in range(len(arr2[0])):
        for i in range(len(arr1)):
            temp = 0
            for j in range(len(arr2)):
                temp += arr1[i][j] * arr2[j][k]
            arr3[i][k] = temp
    return arr3


print(solution(arr1, arr2))
