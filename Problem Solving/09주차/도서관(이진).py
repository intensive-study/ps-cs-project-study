import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())
location = list(map(int, input().split()))
positive, negative = [], []

max_distance = max(abs(min(location)), abs(max(location)))

for loc in location:
    if loc > 0:
        positive.append(loc)

    else: # loc < 0
        negative.append(abs(loc))

def append_dist(target_list, m):
    for i in range(0, len(target_list), m):
        if target_list[i] != max_distance:
            answer.append(target_list[i])
    return answer

positive.sort(reverse=True)
negative.sort(reverse=True)
answer = []
answer = append_dist(positive, m)
answer = append_dist(negative, m)
total = 0
for ans in answer:
    total += (ans*2)
total += max_distance

print(total)