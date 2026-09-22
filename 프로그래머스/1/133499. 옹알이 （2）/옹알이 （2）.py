def solution(babbling):
    answer = 0
    joka = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        word = babbling[i]
        for j in joka:
            if j + j in word:
                break
            
            word = word.replace(j, ' ')
        
        if word.strip() == '':
            answer += 1
            
    return answer