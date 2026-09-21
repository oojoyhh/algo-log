def solution(k, score):
    answer = []
    minn = []
    for i in range(len(score)):
        minn.append(score[i])

        if len(minn) > k:
            minn.remove(min(minn))
        
        answer.append(min(minn))

    return answer