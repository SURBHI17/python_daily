def factor(num):
    i=1
    print("factors of",num,"are:")
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
def even(num):
    print("even number till",num,":")
    for i in range(2,num+1,2):
        print(i)
        
def perfect(num):
    sum=0
    i=1
    for i in range(1,num):
        if(num%i==0):
            sum+=i 
    if(sum==num):
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")
factor(34)
even(6)
perfect(812)
  