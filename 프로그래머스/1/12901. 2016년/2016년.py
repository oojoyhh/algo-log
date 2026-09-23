def solution(a, b):
    answer = ''
    days = 0
    yoil = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    year = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    
    for i in range(1, a):
        days += year[i]
    
    days = days + (b-1)
    
    return yoil[days%7]