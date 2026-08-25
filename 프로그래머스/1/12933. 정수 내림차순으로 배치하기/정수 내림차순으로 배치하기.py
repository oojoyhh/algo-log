def solution(n):
    answer = sorted([int(x) for x in str(n)], reverse=True)
    ans = ''.join(map(str,answer))
    return int(ans)