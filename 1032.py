import sys

N = int(sys.stdin.readline())
name = sys.stdin.readline()
answer = list(name)

for i in range(N-1):
    name1 = sys.stdin.readline()
    for j in range(len(name)):
        if name[j] != name1[j] and answer[j] != '?':
            answer[j] = '?'

print(''.join(answer))