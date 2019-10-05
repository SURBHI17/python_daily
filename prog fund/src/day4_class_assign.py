def duplicate(value):
    dup=""
    for element in value:   
        if element in dup:      #if element not in value:
            continue            #    dup+=element
        else:                   #    
            dup+=element        #return dup
         
    return dup   
    
value1="popeye"

print(duplicate(value1))