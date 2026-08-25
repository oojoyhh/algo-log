def solution(s):
    pnum, ynum = 0, 0
    answer = True
    
    for i in s:
        if i == 'p' or i == 'P':
            pnum += 1
        elif i == 'y' or i == 'Y':
            ynum += 1
            
    if pnum != ynum:
        answer = False
        
    return answer