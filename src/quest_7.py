#PF-Prac-7
def seed_no(number,ref_no):
    #start writing your code here
    prod=1
    temp=number
    while(number>0):
        rem=number%10
        prod*=rem
        number//=10
    if(prod*temp==ref_no):
        return True
    else:
        return False
    
    
number=123
ref_no=738
print(seed_no(number,ref_no))