def solution(s):
    ans = sorted(s)
    small = []
    big = []
    total = ''
    
    for idx, char in enumerate(ans):
        if char == ans[idx].lower():
            small.append(char)
        else:
            big.append(char)
            
    small = sorted(small, reverse=True)
    big = sorted(big, reverse=True)
    total = ''.join(small + big)
    return total