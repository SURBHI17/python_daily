#PF-Assgn-42
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and  --> i and returns True if the number is 
    #prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))
 
def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    prime_list=[] 
    for el in list_of_factors:
        if is_prime(el,el//2)==True:
            prime_list.append(el)
    return max(prime_list)
 
def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    list=find_factors(num)
    return find_largest_prime_factor(list)
 
def find_g(num):
    sum1=0
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    for i in range(0,9):
        sum1+=find_f(num)
        num+=1
    return sum1
# 
print(find_g(10))
