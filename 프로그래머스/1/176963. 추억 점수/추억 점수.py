def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        hap = 0
        for n in range(len(p)):
            if p[n] in name:
                hap += yearning[name.index(p[n])]
        answer.append(hap)
    return answer