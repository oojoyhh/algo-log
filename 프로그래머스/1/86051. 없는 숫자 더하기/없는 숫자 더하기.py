def solution(numbers):
    answer = -1
    nums = [1,2,3,4,5,6,7,8,9,0]
    ans = [x for x in nums if x not in numbers]
    answer = sum(ans)
    return answer