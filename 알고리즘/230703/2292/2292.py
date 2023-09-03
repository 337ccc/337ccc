import sys
sys.stdin = open("sample.txt")

N = int(sys.stdin.readline().strip())

answer = 1
num = 1
while N > num:
    num += answer * 6
    answer += 1

print(answer)