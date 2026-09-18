def solution(food):
    ans = ''
    for i in range(len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        ans += str(i) * (food[i]//2)
    
    reans = ''.join(sorted(ans, reverse=True))
    return ans + '0' + reans