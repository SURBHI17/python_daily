#PF-Assgn-47
def encrypt_sentence(sentence):
    list1=sentence.split()
    reverse=""
    for el in list1:
        if list1.index(el)%2==0:
            el=el[::-1]
        else:
            vowel=[]
            cons=[]
            el=list(el)
            
            for i in el:
                
                if i in ["a","e","i","o","u"]:
                    vowel.append(i)
                else:cons.append(i)
            el=""
            
            for item in cons:
                el+=item
            for item in vowel:
                el+=item
    
        reverse+=el+" "
    reverse=reverse[:-1]
    return reverse
         
     

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)