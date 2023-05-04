import sys

N, K = list(map(int, sys.stdin.readline().split()))
coin = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
cnt = 0

for c in coin:
    if K / c >= 1:
        cnt += int(K / c)
        K = K % c

print(cnt)