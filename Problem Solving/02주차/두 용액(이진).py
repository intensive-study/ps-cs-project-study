import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))  # -2 4 -99 -1 98

solution.sort() # [-99, -2, -1, 4, 98]

left, right = 0, len(solution) - 1
min_left, min_right = 0, len(solution) -1
mixed = abs(solution[left] + solution[right])

while left < right:
	tmp = solution[left] + solution[right]
	if abs(tmp) < mixed:
		mixed = abs(tmp)
		min_left, min_right = left, right
	if tmp == 0:
		break
	elif tmp > 0:
		right -= 1
	else: # tmp < 0
		left += 1

print(solution[min_left], solution[min_right])