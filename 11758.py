import sys

x1, y1 = list(map(int, sys.stdin.readline().split()))
x2, y2 = list(map(int, sys.stdin.readline().split()))
x3, y3 = list(map(int, sys.stdin.readline().split()))

ccw = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

if ccw == 0:
    print(0)
elif ccw > 0:
    print(1)
else:
    print(-1)