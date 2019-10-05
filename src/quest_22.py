#PF-Tryout
def diagonal_stars(number):
    #start writing your code here
    a=""
    for i in range(0,number):
        a+="."*i+"*"
        print(a)
        a=""
   
number=6    
diagonal_stars(number)