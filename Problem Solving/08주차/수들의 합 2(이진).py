'''124ms'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))

left, right = 0, 0
total = 0
count = 0


while True:
    if total >= m:
        total -= a[left]
        left += 1
    elif right == n:
        break
    else:
        total += a[right]
        right += 1

    if total == m:
        count += 1


print(count)		