def solution(s):
    answer = []
    already = {}

    for idx, chr in enumerate(s):
        if chr not in already:
            answer.append(-1)
        else:
            answer.append(idx-already[chr])
        already[chr] = idx
    return answer