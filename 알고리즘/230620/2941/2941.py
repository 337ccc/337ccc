import sys
sys.stdin = open("sample.txt")

word = sys.stdin.readline().strip()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in croatia:
    word = word.replace(i, "a")

word = list(word)
print(len(word))