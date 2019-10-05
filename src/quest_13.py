#PF-Tryout
def find_five_digit():
    #start writing your code here
    number=0
    for a3 in range(2,5):
        a2= a3 + 2
        a1= a2 + 2
        a4= a3 - 2
        a5= a4 + 2
        if a3 + a4 + a5== a1:
            if 2*a1 + a2==19:
                number=number+a5+(a4*10)+(a3*100)+(a2*1000)+(a1*10000)
    return number

print(find_five_digit())