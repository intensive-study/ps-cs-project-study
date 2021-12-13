# ms

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() # 1 2 3 4 5

def binary_search(target_list, target_elem):
	left, right = 0, len(target_list)-1
	
	while left <= right:
		mid = (left + right) // 2

		if target_list[mid] == target_elem:
			return True
		
		if target_elem < target_list[mid]:
			right = mid-1  ## 시간초과!
		else: # target_elem > target_list[mid]
			left = mid+1  ## 시간초과!


for m_elem in m_list:
	if binary_search(n_list, m_elem): # m_elem이 n_list안에 존재한다면
		print(1)
	else:
		print(0)