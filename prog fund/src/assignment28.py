#PF-Assgn-28


def find_max(num1, num2):
    max_num=-1
    list1=[]
    # Write your logic here
    if(num1>=num2):
        return max_num
    else:
        for i in range(num1,num2+1):
            sum = (i%10+i//10)
            if ((i>=10 and i<=99) and (i%5==0) and sum%3==0):
                list1.append(i)
            
         
        if(len(list1)==0):
            return max_num
            
    max_num=list1[len(list1)-1]
    
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)