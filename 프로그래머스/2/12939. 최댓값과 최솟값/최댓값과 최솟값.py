def solution(s):
    nums = s.split()
    
    for i in range(len(nums)):
        nums[i] =int(nums[i])
        
    minn = min(nums)
    maxx = max(nums)
    return str(minn) + " " + str(maxx)