from collections import deque

if __name__ == '__main__':
    N = int(input())
    str_array = input()
    cnt = set([str_array[0]])
    dq = deque()
    dq.append(str_array[0])
    answer = 0

    right = 1
    while dq:
        while len(cnt) <= N and right < len(str_array):
            dq.append(str_array[right])
            cnt.add(str_array[right])
            right += 1

        if len(str_array) == right:
            if len(cnt) > N:
                answer = max(len(dq)-1, answer)
                break
            else:
                answer = max(len(dq), answer)
                break


        tmp = dq.popleft()
        answer = max(len(dq), answer)

        while tmp in dq:
            tmp = dq.popleft()
        if tmp in cnt:
            cnt.remove(tmp)

    print(answer)

"""
2
abbcaccba
result = 4

5
aaaaa
result = 5

2
abca
result = 2
"""
