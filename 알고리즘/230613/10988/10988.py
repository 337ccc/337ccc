import sys
sys.stdin = open("sample.txt")

word = list(input())

answer = 1
N = len(word) // 2
for i in range(N):
    if word[i] != word[len(word) - 1 - i]:
        answer = 0
        break

print(answer)