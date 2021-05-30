import bisect

def solution(words, queries):
    words_sorted = [[] for _ in range(10000)]
    words_sorted_reverse = [[] for _ in range(10000)]
    for word in words:
        words_sorted[len(word)-1].append(word)
        word_reverse = word[::-1]
        words_sorted_reverse[len(word)-1].append(word_reverse)
    for i in range(len(words_sorted)):
        words_sorted[i].sort()
        words_sorted_reverse[i].sort()
    dict = {}
    answer = [0 for _ in range(len(queries))]
    i = 0
    for query in queries:
        if not query in dict.keys():
            if query[0] == '?':
                query = query[::-1]
                target_list = words_sorted_reverse[len(query)-1]
                query_left = query.replace('?', 'a')
                query_right = query.replace('?', 'z')
                l = bisect.bisect_left(target_list, query_left)
                r = bisect.bisect_right(target_list, query_right)
                query = query[::-1]
                dict[query] = r - l
            else:
                target_list = words_sorted[len(query) - 1]
                query_left = query.replace('?','a')
                query_right = query.replace('?','z')
                l = bisect.bisect_left(target_list, query_left)
                r = bisect.bisect_right(target_list, query_right)
                dict[query] = r-l
        answer[i] = dict[query]
        i += 1
    # print(dict)
    return answer
