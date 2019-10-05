#PF-Prac-13
def close_number(num1,num2,num3):
    #start writing your code here
    if abs(num1-num2)<=1 and abs(num3-num2)>1 and abs(num3-num1)>1:
        return True
    elif abs(num2-num3)<=1 and abs(num1-num2)>1 and abs(num1-num3)>1:
        return True
    elif abs(num3-num1)<=1 and abs(num2-num1)>1 and abs(num2-num3)>1:
        return True
    else:
        return False
    
print(close_number(5,4,2))