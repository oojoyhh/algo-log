def solution(s):
    answer = ''
    for word in s.split(' '):
        for j, char in enumerate(word):
            if j % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        answer += ' '
    return answer[:-1]