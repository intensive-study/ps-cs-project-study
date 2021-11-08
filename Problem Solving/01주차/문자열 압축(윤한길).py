import re


def solution(s):
    length = len(s)
    max_length = length // 2
    possible_cases = []

    for i in range(1, max_length + 1):
        tmp = re.findall('.{%d}|.+' % i, s)
        # print(tmp)

        cnt = 1
        str_tmp = ''
        for j in range(len(tmp)):
            if j < len(tmp) - 1 and tmp[j] == tmp[j + 1]:
                cnt += 1
            else:
                if cnt == 1:
                    str_tmp += tmp[j]
                else:
                    str_tmp += str(cnt) + tmp[j]
                    cnt = 1
        possible_cases.append(len(str_tmp))

    if possible_cases:
        return min(possible_cases)
    else:
        return 1


if __name__ == '__main__':
    l = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd", '']
    for i in l:
        print(solution(i))
