#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    countU=0
    countL=0
    result_list=[]
    for el in sentence:
        if el>="a" and el<="z":
            countL+=1
        elif el>="A" and el<="Z":
            countU+=1
    result_list.append(countU)
    result_list.append(countL)
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))