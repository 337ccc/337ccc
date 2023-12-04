def Counting_Sort(A, B, k):  # k는 범위
    C = [0] * (k + 1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(B) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

arr_data = [0, 4, 1, 3, 1, 2, 4, 1]
arr_temp = [0] * len(arr_data)
Counting_Sort(arr_data, arr_temp, 4)
print(arr_temp)