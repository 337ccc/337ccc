import sys
sys.stdin = open("sample.txt")

num, notation = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ""
while num != 0:
    answer = arr[num % notation] + answer
    num = num // notation

print(answer)