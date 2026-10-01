def solution(s, skip, index):
    idx = 0
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for sk in skip:
        alpha.remove(sk)
        
    for i in range(len(s)):
        idx = alpha.index(s[i])
        new_idx = (idx+index) % len(alpha)
        answer += alpha[new_idx]
    return answer