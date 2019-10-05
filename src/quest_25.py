#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for el in word_list:
        count_list.append(len(el))
    #start writing your code here
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))