def findRepeatNumber(nums):
    n=len(nums)
    res=[]
    for i in range(n):
        while nums[i]!=i:
            if nums[i]==nums[nums[i]]:
                res.append(nums[i])
                break
            a,b= nums[i], nums[nums[i]]
            nums[i], nums[a]=b,a
    return res

def findRepeatNumber2(nums):
    n=len(nums)
    res=[]
    for i in range(n):
        if nums[abs(nums[i])]<0:
            res.append(abs(nums[i]))
            continue
        nums[abs(nums[i])]=-nums[abs(nums[i])]

    return res

print(findRepeatNumber2([2,3,1,4,2,5,3]))