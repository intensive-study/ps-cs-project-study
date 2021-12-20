import sys

input = sys.stdin.readline

def solve(n, record):
    table = [-int(2e9)-int(5e8)] * (n)
    table[0] = record[0]

    for i in range(1, n):
        table[i] = max(table[i-1] + record[i], record[i])
    
    return max(table)

if __name__ == "__main__":
    while True:
        n = int(input())
        if not n: break
        record = [int(input()) for _ in range(n)]
        print(solve(n, record))