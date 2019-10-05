#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    average=[]
    avg=0
    pass1=0
    average=list(list_of_marks)
    for el in average:
        avg+=el
    avg=avg/len(average)
    for el in average:
        if el>avg:
            pass1+=1
    pass1=pass1/len(average)*100
    return pass1   


def sort_marks():
    return sorted(list(list_of_marks))
    

def generate_frequency():
    freq=[]
    list_of_marks=sort_marks()
    count=0
    for i in range(0,26):
        count=0
        for j in list_of_marks:
            if(i==j):
                count+=1
        freq.append(count)
           
    return freq  
            
            
        
    

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())