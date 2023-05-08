import sys

T = int(sys.stdin.readline())

for _ in range(T):
    tmp = []
    ps = sys.stdin.readline()

    for i in ps[:-1]:
        if len(tmp) == 0:
            tmp.append(i)
        else:
            if tmp[-1] == '(' and i ==')':
                tmp = tmp[:-1]
            else:
                tmp.append(i)

    if len(tmp) == 0:
        print("YES")
    else:
        print("NO")