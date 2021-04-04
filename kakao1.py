def solution(s):
    if len(s) < 3:
        return len(s)
    answer = 1000
    for i in range(1, int(len(s)/2)+1):
        memory = s[0:i]
        cnt = 1
        now_ans = 0
        for j in range(i, len(s), i):
            if j+i > len(s):
                now_ans += len(s) - j
                break
            token = s[j:j+i]
            if memory == token:
                cnt += 1
            else:
                now_ans += len(memory)
                if cnt > 1:
                    now_ans += len(str(cnt))
                memory = token
                cnt = 1
        now_ans += len(token)
        if cnt > 1:
            now_ans += len(str(cnt))
        answer = min(answer, now_ans)
    return answer
