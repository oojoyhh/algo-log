def solution(polynomial):
    xans = 0   # x의 계수 합
    num = 0    # 상수 합

    for p in polynomial.split(' '):
        if p == '+':
            continue

        if p.endswith('x'):
            # x만 있으면 계수가 1
            if p == 'x':
                xans += 1
            else:
                xans += int(p[:-1])
        else:
            num += int(p)

    answer = []

    if xans == 1:
        answer.append('x')
    elif xans > 1:
        answer.append(str(xans) + 'x')

    if num > 0:
        answer.append(str(num))

    return ' + '.join(answer)