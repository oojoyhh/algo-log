def solution(n):
    s = n ** 0.5
    if s == int(s):
        return (s+1)**2

    else:
        return -1