import sys
sys.stdin = open("sample.txt")

N = int(input())
result = [int(sys.stdin.readline().strip()) for _ in range(1, N + 1)]
# 오름차순 : 작은 수 -> 큰 수
# stack에 push하는 순서는 반드시 오름차순
stack = []
backward = []
answer = []

# 늘어놓은 수들을 거꾸로 다시 stack에 넣음
# 그 과정에서 1부터 N까지 수가 거꾸로 backward에 들어감
# 그리고 push, pop 과정이 거꾸로 진행됨
while len(backward) != N:
    # result가 비어있지 않다면
    if result:
        if not stack or stack[-1] < result[-1]:
            i = result.pop()
            stack.append(i)
            answer.append("-")
        else:
            factor = stack.pop()
            if not backward or backward[-1] > factor:
                backward.append(factor)
                answer.append("+")
            else:
                answer = "NO"
                break
    # result가 비어도 stack은 아직 비어있지 않기 때문에
    # stack 수를 backward 쪽으로 이동해야 함
    else:
        factor = stack.pop()
        if not backward or backward[-1] > factor:
            backward.append(factor)
            answer.append("+")
        else:
            answer = ["NO"]
            break

if result:
    print(answer)
else:
    for j in range(len(answer) - 1, -1, -1):
        print(answer[j])

# 1)
# 4 3 6 8 7 5 2 1
# stack = []
# backward = []
# answer = []

# 2) 오름차순 규칙 때문에 6을 stack에 넣을 수 없음
# 4 3 6
# stack = [1 2 5 7 8]
# backward = []
# answer = [- - - - -]

# 3) 오름차순 규칙 때문에 3을 stack에 넣을 수 없음
# 4 3
# stack = [1 2 5 6]
# backward = [8 7]
# answer = [- - - - - + + -]

# 4)
#
# stack = [1 2 3 4]
# backward = [8 7 6 5]
# answer = [- - - - - + + - + + - -]

# 5)
#
# stack = []
# backward = [8 7 6 5 4 3 2 1]
# answer = [- - - - - + + - + + - - + + + +]

# answer를 거꾸로 출력