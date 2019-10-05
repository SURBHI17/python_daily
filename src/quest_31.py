#PF-Prac-31
def sum_of_elements(num_list,number):
    result_sum=0
    l=len(num_list)
    i=0
    
    while(i<l-1):
        if num_list[i]==number:
            i=i+2
        elif num_list[i+1]!=number:
            result_sum+=num_list[i]
            i=i+1
        else: i=i+1   
    if i<l and num_list[i]!=number and num_list[i-1]!=number:
        
        result_sum+=num_list[i]

    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))