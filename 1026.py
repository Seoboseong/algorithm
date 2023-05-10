import sys

N = int(sys.stdin.readline())
answer = 0

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for i, j in zip(sorted(A), sorted(B, reverse=True)):
    answer += i * j

print(answer)