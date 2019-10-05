#day 3 class assignment
#function to find factorial of a number
def fact1(num):
    factorial=1
    temp=num
    while(num>1):
        factorial=factorial*num
        num=num-1
    print(factorial,"is factorial of",temp)
    
#funtion to check palindrome
def palin(num):
    temp=num
    reverse=0
    while(num!=0):
        remainder=num%10
        reverse=reverse*10+remainder
        num=num//10
    if(reverse==temp):
        print(temp,"is a palindrome")
    else:
        print(temp,"is not a palindrome")
        
fact1(5)
palin(121)