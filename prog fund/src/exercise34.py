#PF-Exer-34
import math

def find_number_of_combination(number_of_flavours):
    total_combination=0
    r=number_of_flavours
    n=number_of_flavours
    
    while(r>=0):
        total_combination+=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
        r-=1
    
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)