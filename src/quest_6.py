#PF-Prac-6
def list123(nums):
    l=len(nums)
    i=0
    while(l>0 and i<l-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
        
        i+=1
    return False
nums=[1,2,3]
print(list123(nums))