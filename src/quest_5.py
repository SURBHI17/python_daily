#PF-Prac-5
def count_digits_letters(sentence):
    cound_digit=0
    count_letter=0
    result_list=[]
    for el in sentence:
        if (el>="a" and el<="z") or (el>="A" and el<="Z"):
            count_letter+=1
        elif el>="0" and el<="9":
            cound_digit+=1
            
    result_list.append(count_letter)
    result_list.append(cound_digit)
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))