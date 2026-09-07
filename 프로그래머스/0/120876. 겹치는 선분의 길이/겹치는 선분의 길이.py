def solution(lines):
    answer = []
    result = 0
    jum = [0]*201
    for i in lines:
        for j in range(i[0], i[1]):
            jum[j+100] += 1
            
    for k in jum:
        if k > 1:
            result += 1
    return result