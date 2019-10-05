#PF-Prac-4
def find_nine(nums):
    for el in nums[:4:]:
        if el==9:
            return True
        
    else:
            return False

nums=[1,9,4,5,6]
print(find_nine(nums))