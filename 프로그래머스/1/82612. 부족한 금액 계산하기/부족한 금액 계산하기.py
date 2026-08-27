def solution(price, money, count):
    answer = 0
    total = (price+(count*price))*(count/2)
    if money - total < 0:
        answer = total - money
    
    return answer