import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

neg = []
pos = []
for n in arr:
    if n < 0: neg.append(n)
    elif n > 0: pos.append(n)

neg.sort()
pos.sort(reverse=True)
nflag, pflag = True, True
if neg and pos:
    if abs(neg[0]) > pos[0]: pflag = False
    else: nflag = False

elif not neg: nflag = False
elif not pos: pflag = False

neg_len = len(neg)
i = 0
answer = 0

while i < neg_len:
    if i + m < neg_len:
        if i == 0 and nflag: answer += abs(neg[i])
        else: answer += abs(neg[i]) * 2
        i += m
    
    else:
        if i == 0 and nflag: answer += abs(neg[i])
        else: answer += abs(neg[i]) * 2
        i = neg_len

pos_len = len(pos)
i = 0

while i < pos_len:
    if i + m < pos_len:
        if i == 0 and pflag: answer += pos[i]
        else: answer += pos[i] * 2
        i += m 
    
    else:
        if i == 0 and pflag: answer += pos[i]
        else: answer += pos[i] * 2
        i = pos_len

print(answer)