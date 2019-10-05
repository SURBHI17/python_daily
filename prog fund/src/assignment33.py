#PF-Assgn-33

def find_common_characters(msg1,msg2):
    common1=""
    
    for el in msg1:
        if el==" " or el in common1:
            continue
        
        elif el in msg2:
            common1+=el
        
    if(common1==""):
        return -1
    else:
        return common1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)    
print(common_characters)