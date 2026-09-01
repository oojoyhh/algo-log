from itertools import permutations
def solution(babbling):
    cnt = 0
    can = ['aya', 'ye', 'woo', 'ma', 'ayayewooma']
    for k in permutations(can,2):
        can.append(''.join(k))
    
    for k in permutations(can,3):
        can.append(''.join(k))
        
    for i in babbling:
        if i in can:
            cnt += 1
    return cnt