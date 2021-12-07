import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
p = [-1] * (n+1)

def find(x):
    if p[x] < 0:
        return x
    else:
        y = find(p[x])
        p[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[y] = x


for i in range(n):
    connection = list(map(int, input().split()))
    for j in range(i+1, n):
        if connection[j]:
            union(i+1, j+1)
flag = True
travelPlan = list(map(int, input().split()))
tmp = find(travelPlan[0])
for i in range(m):
    if find(travelPlan[i]) != tmp:
        flag = False
        break
        
if flag:
    print("YES")
else:
    print("NO")