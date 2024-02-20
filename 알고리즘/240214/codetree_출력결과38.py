arr = [[0, 0, 1],
       [1, 0, 0],
       [0, 1, 0]]

for k in range(3):
    for i in range(3):
        for j in range(3):
            if arr[i][k] and arr[k][j]:  # 둘 다 1이면
                arr[i][j] = 1

            print(k, i, j)
            for line in range(3):
                print(arr[line])

result = 0
for i in range(3):
    result += sum(arr[i])
print(result)