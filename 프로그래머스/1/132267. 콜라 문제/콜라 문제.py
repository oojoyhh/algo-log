def solution(a, b, n):
    cnt = 0
    while n >= a:
        got = n//a *b
        cnt += got
        n = n % a + got
    return cnt