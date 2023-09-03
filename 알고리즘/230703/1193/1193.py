import sys
sys.stdin = open("sample.txt")

N = int(sys.stdin.readline().strip())

answer = 0
# num = 몇 번째 줄인지
num = 1
while answer + num < N:
    answer += num
    num += 1

# total = 분자와 분모의 합
total = num + 1
N = N - answer
if num % 2 == 0:
    print(f"{N}/{total - N}")
else:
    print(f"{total - N}/{N}")