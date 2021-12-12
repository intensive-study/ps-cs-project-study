import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
m = int(input())
sys.setrecursionlimit(int(1e4))


def solve(k):
    global m