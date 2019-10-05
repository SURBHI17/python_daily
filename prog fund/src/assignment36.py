#PF-Assgn-36
from _ast import Num
def create_largest_number(number_list):
    largest_number=[]
    str1=""
    largest_number=sorted(number_list)
    largest_number=largest_number[::-1]
    for el in largest_number:
        str1+=str(el)
    
    return int(str1)
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)