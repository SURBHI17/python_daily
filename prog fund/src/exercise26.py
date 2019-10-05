#PF-Exer-26

def factorial(number):
    fact=1
    while number>1:
        fact*=number
        number-=1
    return fact


def find_strong_numbers(num_list):
    strong_list=[]
    for el in num_list:
        temp=el
        sum1=0
        while temp>0:
            rem=temp%10
            sum1+=factorial(rem)
            temp=temp//10
        if sum1==el and el!=0:
            strong_list.append(el)
    return strong_list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)