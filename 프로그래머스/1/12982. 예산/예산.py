def solution(d, budget):
    cnt = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            cnt += 1
        else:
            break
        
    return cnt