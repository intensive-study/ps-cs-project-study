def solution(s):
    answer_len = []  # 모든 답안의 길이 저장하는 변수

    if len(s) == 1:  # 이거 안하면 testcase5 통과 못함
        return 1

    for digit in range(1, len(s) // 2 + 1):  # 슬라이싱 개수를 1~절반까지
        answer = ""
        cnt = 1
        tmp = s[:digit]

        for j in range(digit, len(s), digit):
            new_tmp = s[j:j+digit]  # 그 다음 슬라이싱한 문자열
            if new_tmp == tmp: # 앞과 같으면 개수 추가
                cnt += 1
            else:  # 앞과 다른 새로운 문자열이면
                if cnt > 1: # 이전의 반복됐던 문자열 저장하고
                    tmp = str(cnt) + tmp
                    cnt = 1
                answer += tmp
                tmp = new_tmp  # 새로운 문자열을 tmp로 할당함.
        # for문이 끝난 후 마지막 문자열이 남게됨.
        if cnt > 1:
            tmp = str(cnt) + tmp
        answer += tmp
        # print(answer)
        answer_len.append(len(answer))

    return min(answer_len)

# 스택 이용
# def solution(s):
#     answer_len = []
#
#     if len(s) == 1:
#         return 1
#
#     for i in range(1, len(s) // 2 + 1):
#         lst = [s[j:j + i] for j in range(0, len(s), i)]
#         new_lst = []
#         answer = ""
#         new_lst.append(lst.pop(0))
#         cnt = 1
#         while lst:
#             elem = lst.pop(0)
#             if elem == new_lst[-1]:
#                 cnt += 1
#             else:
#                 if cnt > 1:
#                     answer += str(cnt) + new_lst.pop()
#                 else:
#                     answer += new_lst.pop()
#                 new_lst.append(elem)
#                 cnt = 1
#         if cnt > 1:
#             answer += str(cnt) + new_lst.pop()
#         else:
#             answer += new_lst.pop()
#         answer_len.append(len(answer))
#     return min(answer_len)

s = 'xababcdcdababcdcd'
print(solution(s))