#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    length=len(num_list)
    count=0
    s=1
    for j in range(0,length-1):
        for i in range(s,length):
            if num_list[j]+num_list[i]==n: 
                #+num_list[i]
                count+=1
        s=s+1  
    return count
            
        

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))