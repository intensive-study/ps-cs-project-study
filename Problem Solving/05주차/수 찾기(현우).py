import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dic = {}
arr = list(map(int, input().split()))
for i in arr:
    dic[i] = 1
M = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in dic:
        print(1)
    else:
        print(0)
