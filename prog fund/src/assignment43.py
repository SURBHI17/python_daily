#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    number=1
    while number>0:
        count=1
        for j in range(2,number+1):
            if number%j==0:
                count+=1
        if count==num:
            return number
        number+=1
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)