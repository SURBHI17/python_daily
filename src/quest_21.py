#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    num_list=[]
    count=0
    for i in range(num1,num2+1):
        for j in range(num1,i):
            if i%j==0 and j!=i and i not in num_list:
                num_list.append(i)
    num_list=set(num_list)
    count=len(num_list)
    return [num_list,count]

num1=100
num2=200
print(check_numbers(num1, num2))