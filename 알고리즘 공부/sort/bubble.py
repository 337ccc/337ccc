arr = [55, 7, 78, 12, 42]
N = len(arr)

for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)  # [7, 12, 42, 55, 78]
print(*arr)  # 7 12 42 55 78


arr = [55, 7, 54, 12, 42]
N = len(arr)
maxV = arr[0]

for i in range(N):
    if arr[i] > maxV:
        maxV = arr[i]
print(maxV)  # 55