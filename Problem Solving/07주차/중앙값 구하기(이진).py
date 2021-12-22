import sys
import heapq
input = sys.stdin.readline

def find_median(lst):
	left_heap, right_heap = [], []
	med = lst[0]
	med_lst = [med]

	for i, v in enumerate(lst[1:]):
		if v > med:
			heapq.heappush(right_heap, v)
		else:
			heapq.heappush(left_heap, -v)
		if i % 2 == 0:
			if len(left_heap) > len(right_heap):
				heapq.heappush(right_heap, med)
				med = -heapq.heappop(left_heap)
			elif len(left_heap) < len(right_heap):
				heapq.heappush(left_heap, -med)
				med = heapq.heappop(right_heap)
			med_lst.append(med)
	return med_lst


for _ in range(int(input())):
	m = int(input())
	lst = []
	
	line = m // 10
	left = m % 10

	if left == 0: #10의 배수로 딱 떨어지는 경우
		for _ in range(line):
			lst.extend(list(map(int, input().split())))
	else: # 나머지가 생기는 경우
		for _ in range(line + 1):
			lst.extend(list(map(int, input().split())))

	med_lst = find_median(lst)
	print(len(med_lst))
	for i in range(len(med_lst)):
		if i > 0 and i % 10 == 0:
			print()
		print(med_lst[i], end=' ')
	print()