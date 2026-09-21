def two_sum(nums,target):
    mpp={}
    for i in range(len(nums)):
        num=target-nums[i]
        if num in mpp:
            return [i,mpp[num]]
        mpp[nums[i]]=i
    return
print(two_sum([2,7,5,3,5,3],9))