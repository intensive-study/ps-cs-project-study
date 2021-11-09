import re
from collections import defaultdict


# 두번째 예제는 통과 못함.
# def solution(word, pages):
#
#     score_dict = defaultdict(int)
#
#     for page in pages:
#         url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
#         score = 0
#         # print(url)
#
#         # 기본 점수
#         for find_word in re.findall(r'[A-Za-z]+', page.lower()):
#             if find_word == word.lower():
#                 score += 1
#         score_dict[url] = score
#
#         # 외부 링크 수
#         external_link = re.findall('<a href="(https://[\S]*)"', page)
#         # print(external_link)
#
#         # 링크 점수
#         link_score = score / len(external_link)
#
#         # 연결된 링크
#         for link in external_link:
#             score_dict[link] += link_score
#
#     lst = list(score_dict.values())
#
#     return lst.index(max(lst))


# 테스트10-14 런타임 에러 => 75점
# def solution(word, pages):
#
#     score_dict = defaultdict(int)
#     link_score_dict = defaultdict(int)
#     link_dict = defaultdict(list)
#
#     for page in pages:
#         url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
#         score = 0
#
#         # 기본 점수
#         for find_word in re.findall(r'[A-Za-z]+', page.lower()):
#             if find_word == word.lower():
#                 score += 1
#         score_dict[url] += score
#
#         external_link = re.findall('<a href="(https://[\S]*)"', page)
#         link_dict[url] = external_link
#         link_score_dict[url] = score / len(external_link)
#
#     for key, values in link_dict.items():
#         # print(k,v)
#         for v in values:
#             if v in score_dict:
#                 score_dict[v] += link_score_dict[key]
#
#     lst = list(score_dict.values())
#     return lst.index(max(lst))


def solution(word, pages):

    score_dict = defaultdict(list)
    url_lst = []
    link_dict = defaultdict(list)

    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        url_lst.append(url)
        score = 0

        for find_word in re.findall(r'[A-Za-z]+', page.lower()):
            if find_word == word.lower():
                score += 1
        score_dict[url].append(score)  # 기본 점수

        external_link = re.findall('<a href="(https://[\S]*)"', page)
        score_dict[url].append(len(external_link))      # 링크 개수  # [3, 1] 형식으로 저장됨.

        for link in external_link:
            link_dict[link].append(url)

    score_lst = []
    for url in url_lst:
        score = score_dict[url][0]  #기본 점수 설정
        for link in link_dict[url]:
            score += (score_dict[link][0] / score_dict[link][1])  # 링크 점수 더해주기
        score_lst.append(score)
    return score_lst.index(max(score_lst))


word = 'Muzi'
pages =["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))
