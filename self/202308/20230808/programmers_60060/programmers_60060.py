def solution(words, queries):
    answer = []

    for query in queries:

        N = len(query)
        question_mark = 0
        check_query = list(query)
        front_or_rear = 0

        while check_query[0] == '?':
            check_query.pop(0)
            question_mark += 1
            front_or_rear = 1

        while check_query[-1] == '?':
            check_query.pop()
            question_mark += 1
            front_or_rear = -1


        cnt = 0
        for word in words:
            if len(word) == N:
                if front_or_rear == 1:
                    if list(word)[question_mark:] == check_query:
                        cnt += 1
                elif front_or_rear == -1:
                    if list(word)[:N-question_mark] == check_query:
                        cnt += 1

        answer.append(cnt)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))

# result = [3, 2, 4, 1, 0]

# 확인용
# print(len(words[0]))
# print((list(words[0])).pop(0))