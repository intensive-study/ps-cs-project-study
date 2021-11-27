import sys
from collections import defaultdict, Counter, deque
input = sys.stdin.readline

N = int(input().rstrip())
lst = list(map(int, input().split()))

'''시간초과
fdict = defaultdict(int)
answer = []

for i in lst:
    fdict[i] += 1

for i in range(len(lst)):
    flag = False
    target = lst[i]
    for elem in lst[i+1:]:
        if target == elem:
            continue
        if fdict[target] < fdict[elem]:
            answer.append(elem)
            flag = True
            break
    if not flag:
        answer.append(-1)
        
print(*answer)
'''

''' 1180ms
stack = []
n = int(input())
lst = list(map(int, input().split()))
cnt = collections.Counter(lst)
s = [[cnt[num], int(num)]for num in lst]
answer = [-1 for _ in range(len(lst))]
stack.append(0)

i= 1

while stack and i < len(lst):
    while stack and s[stack[-1]][0] < s[i][0]:
        answer[stack.pop()] = s[i][1]
        
    stack.append(i)
    i+=1
print(*answer)    
'''


#924ms
N = int(input().rstrip())
lst = list(map(int, input().split()))

stack = []
cnt = Counter(lst)
answer = [-1 for _ in range(len(lst))]

for i in range(len(lst)):
    while stack and cnt[lst[stack[-1]]] < cnt[lst[i]]:
        answer[stack.pop()] = lst[i]
    stack.append(i)
print(*answer)
