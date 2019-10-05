#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    last=[]
    last=number_list[-len(number_list)//2:]
    last=last[::-1]
    first=number_list[:len(number_list)//2]
    l=len(number_list)
    i=0
    while i<l:
        for el in last:
            number_list[i]=el
            i+=1
        for el in first:
            number_list[i]=el
            i+=1
   

    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))