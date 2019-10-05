#PF-Prac-32
import math
from math import ceil
def check_squares(number):
    #start writing your code here
    a=ceil(math.sqrt(number))
    for i in range(a,0,-1):
        for j in range(0,a+1):
            if i*i+j*j==number:
                return True

    return False


number=102
print(check_squares(number))