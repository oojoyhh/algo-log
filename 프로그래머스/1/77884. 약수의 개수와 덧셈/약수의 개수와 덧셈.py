def solution(left, right):
    lst = [x for x in range(left, right+1)]
    ans = sum(lst)
    for i in lst:
        if (i ** 0.5) == int(i ** 0.5):
            ans = ans - i*2
    return ans