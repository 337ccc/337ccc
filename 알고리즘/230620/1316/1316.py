import sys
sys.stdin = open("sample.txt")

N = int(input())

count = N
for _ in range(N):
    word = input()
    word_list = list(word)
    word_alpha = list(set(word))
    for i in word_alpha:
        if word_list.count(i) == 1:
            pass
        else:
            if not i * word_list.count(i) in word:
                count -= 1
                break

print(count)