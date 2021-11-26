
n = int(input())
rslt = [-1] * n
data = list(map(int, input().split()))
dict = dict.fromkeys(data, 0)
stack = [0]

for d in data:
    dict[d] += 1

for i in range(1,n):
    while stack and dict[data[stack[-1]]] < dict[data[i]]:
        rslt[stack[-1]] = data[i]
        stack.pop()

    stack.append(i)

    if not stack:
        break

for re in rslt:
    print(re, end=' ')