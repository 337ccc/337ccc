import sys
sys.stdin = open("sample.txt")

# 알파벳 리스트로 나타내기
from string import ascii_lowercase

alphabet = list(ascii_lowercase)

arr = [-1] * 26

word = list(sys.stdin.readline().strip())
for i in word:
    arr[alphabet.index(i)] = word.index(i)

print(*arr)