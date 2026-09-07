def solution(score):
    total = []
    answer = []
    for i in score:
        total.append(sum(i))
    
    rank = sorted(total, reverse=True)
    
    for i in total:
        answer.append(rank.index(i)+1)
            
    return answer