def solution(a, b):
    naejuk = 0
    for i in range(len(a)):
        naejuk += a[i] * b[i]
    return naejuk