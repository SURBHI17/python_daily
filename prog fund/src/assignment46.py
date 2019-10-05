#PF-Assgn-46

def nearest_palindrome(number):
    while True:
        reverse=0
        number=number+1
        temp=number
        
        while temp>0:
            rem=temp%10
            reverse=reverse*10+rem
            temp//=10
        if reverse==number:
            return number

number=12300
print(nearest_palindrome(number))