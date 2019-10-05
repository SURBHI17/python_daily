#PF-Assgn-44
def find_duplicates(list_of_numbers):
    
    duplicate=[]

    for i in range(len(list_of_numbers)):
        for j in range(i+1,len(list_of_numbers)):
            if list_of_numbers[i]==list_of_numbers[j] and list_of_numbers[i]not in duplicate :
                duplicate.append(list_of_numbers[i])
                break

    return duplicate   

#list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_numbers=[23,32,45,54,32]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)