def solution(phone_number):
    num = phone_number[:-4]
    answer = phone_number.replace(num, '*'*len(num))
    return answer