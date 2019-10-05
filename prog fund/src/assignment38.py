#PF-Assgn-38

def check_double(number):
    double=2*number
    double=str(double)
    number=str(number)
    double=sorted(double)
    number=sorted(number)
    if(len(double)==len(number)):
        i=0
        while(i<len(number)):
            if double[i]!=number[i]:
                return False
            i+=1  
        return True
    else:
        return False
          




print(check_double(125874))