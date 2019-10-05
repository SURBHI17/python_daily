#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
        
    elif((legs-2*heads)%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)//2
        chicken_count= heads- rabbit_count
        print(chicken_count,rabbit_count)
    
        
    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
solve(20,10)


