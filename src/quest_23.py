#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    sum=0
    temp=number
    while(temp>0):
        rem=temp%10
        sum+=rem
        temp//=10
    if number%sum==0:return True
    else: return False

    
number=42
print(divisible_by_sum(number))