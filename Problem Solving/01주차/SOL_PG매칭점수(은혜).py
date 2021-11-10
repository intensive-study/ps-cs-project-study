import re

def solution(word, pages):
    answer = 0
    word = word.lower()
    linkDict = {}

    for idx, page in enumerate(pages):
        url = re.search(r'<meta property="og:url" content="https://(\S+)"', page).group(1)
        body = re.search(r'<body>([\s\S]+)</body>', page).group(1)
        exLink = re.findall(r'<a href="https://([\S]*)"', body) #외부링크 추출
        bdData = re.sub(r'<a href[\s\S]+?/a>', '', body) #외부링크 제거한 데이터(링크에 단어 포함 X)
        score = 0

        for wd in re.findall(r'[a-zA-Z]+', bdData.lower()): #바디 안에 단어 추출
            if wd == word:
                score += 1
                
        for link in exLink:
            if url not in linkDict.keys():
                linkDict[url] = [idx, score, 0, 0, set()] #[인덱스, 기본점수, 외부점수, 링크점수, 외부링크 리스트]순으로 생성
                linkDict[url][4].add(link)
            else:
                linkDict[url][4].add(link) #외부링크 추가  

    #외부 링크 점수 계산
    for key in linkDict:
        cnt = len(linkDict[key][4])
        linkDict[key][2] = cnt 

        for url in linkDict[key][4]:
            if not cnt : break
            if url in linkDict.keys():
                linkDict[url][3] += linkDict[key][1] / cnt #기본점수에 외부링크점수 합
    # 딕셔너리 정렬
    result = sorted(linkDict.items(), key= lambda x : (-(x[1][1]+x[1][3]), x[1][0]))
    answer = result[0][1]

    return answer[0]




word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))

word1 = "Muzi"
pages1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word1, pages1))