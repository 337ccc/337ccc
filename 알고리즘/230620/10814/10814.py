import sys
sys.stdin = open("sample.txt")

N = int(input())

arr = [0] * 201
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if arr[age] == 0:
        arr[age] = [name]
    else:
        arr[age].append(name)

for i in range(201):
    if arr[i] != 0:
        for j in arr[i]:
            print(i, j)