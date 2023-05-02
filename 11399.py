import sys

N = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
output = 0

for idx, value in enumerate(p):
    output += value * (idx+1)
    
print(output)