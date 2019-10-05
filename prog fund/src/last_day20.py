#PF-Prac-20
def ducci_sequence(test_list,n):
    #start writing your code herwhile
    i=0
    temp=[]
    final_list=[]
    while(n>0):
      
        temp=test_list[0]
        test_list[0]=test_list[1]-test_list[0]
        test_list[1]=test_list[2]-test_list[1]
        test_list[2]=test_list[3]-test_list[2]
        test_list[3]= test_list[3]-temp
        n-=1
    while(i<len(test_list)):
        
        final_list.append(test_list[i])
        i+=1
    
    return final_list

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 3)
print(ducci_element)