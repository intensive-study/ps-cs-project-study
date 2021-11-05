from itertools import permutations


def solution(k, dungeons):
    possible_cases = []
    for per in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for i in per:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
        possible_cases.append(cnt)

    return max(possible_cases)


if __name__ == '__main__':
    k, dungeons, result = 80, [[80, 20], [50, 40], [30, 10]], 3
    print(solution(k, dungeons))
