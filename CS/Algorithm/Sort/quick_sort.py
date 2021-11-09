# not stable
# inplace
def quick_sort(l, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:  # 엇갈릴때까지 반복
        while left <= end and l[left] <= l[pivot]:  # pivot보다 큰 데이터를 찾을 때까지 반속
            left += 1
        while right > start and l[right] >= l[pivot]:  # pivot보다 작은 데이터를 찾을 때까지 반속
            right -= 1
        if left > right:  # 엇갈렸다면, 작은 데이터와 pivot을 교체
            l[right], l[pivot] = l[pivot], l[right]
        else:  # 엇갈리지 않았다면, 작은 데이터와 큰 데이터 교체
            l[left], l[right] = l[right], l[left]

        quick_sort(l, start, right - 1)  # 왼쪽 부분
        quick_sort(l, right + 1, end)  # 오른쪽 부분 정렬 수행


if __name__ == '__main__':
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(l, 0, len(l) - 1)
    print(l)

"""
직관적으로 생각하면 [10,9,8,7,6,5,4,3,2,1]을 정렬할때 n^2 = 10^2 = 100 이라면
[10,9,8,7,6], [5,4,3,2,1] 이런식으로 잘게 쪼개 분할 후 각자 정렬 후 나중에 합치면
5^2 = 25
5^2 = 25   ----> 25+25 = 50 ---> 계속 해서 잘게 쪼갠다
"""
