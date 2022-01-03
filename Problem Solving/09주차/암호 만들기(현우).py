import sys

def input():
    return sys.stdin.readline().rstrip()

def check_vowl(st):
    ct = 0
    for i in st:
        if i in vowel:
            ct += 1      
        if ct >= 1:
            return True
    return False

def check_consonant(st):
    ct = 0
    for i in st:
        if i not in vowel:
            ct += 1
        if ct >= 2:
            return True
    return False

def DFS(st, idx):
    if len(st) == N:
        if check_consonant(st) and check_vowl(st):
            ans.append(st)
            return
    for i in range(idx, M):
        DFS(st+arr[i], i+1)

N, M = map(int, input().split())
vowel = set(['a', 'e', 'i', 'o', 'u'])
arr = list(input().split())
arr.sort()
ans = []
DFS('', 0)
for i in ans:
    print(i)