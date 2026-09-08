def solution(numlist, n):
    slist = sorted(numlist, key=lambda x: (abs(n-x), -x))
    return slist