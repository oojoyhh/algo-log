def solution(answers):
    answer = [0, 0, 0]

    n = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == n[j][i%len(n[j])]:
                answer[j] += 1
        
    jinjja = []
    max_score = max(answer)
    
    for k in range(len(answer)):
        if answer[k] == max_score:
            jinjja.append(k+1)
    
    return jinjja