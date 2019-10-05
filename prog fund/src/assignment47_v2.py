#PF-Assgn-47
def encrypt_sentence(sentence):
    list1=sentence.split()
    reverse=""
    for el in list1:
        if list1.index(el)%2==0:
            el=el[::-1]
        else:
            vowel=""
            cons=""
            for i in range(len(el)):  
                if el[i] in ["a","e","i","o","u"]:
                    vowel+=el[i]
                
                else:
                    cons+=el[i]
                    
            el=cons+vowel
    
        reverse+=el+" "
    reverse=reverse[:-1]
    return reverse
         
     

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)