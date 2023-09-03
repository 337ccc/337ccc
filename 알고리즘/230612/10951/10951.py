import sys
sys.stdin = open("sample.txt")

# sys를 사용하는 방법
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    print(A + B)

# EOFError 예외 처리
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break