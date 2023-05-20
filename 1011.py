import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = list(map(int, sys.stdin.readline().split()))

    dist = y-x
    n = int(dist**(1/2))

    if n**2 < dist:
        if n**2 + n < dist:
            count = 2 * n + 1
        else:
            count = 2 * n
    else:
        count = 2 * n - 1

    print(count)