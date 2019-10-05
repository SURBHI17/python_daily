#PF-Assgn-30

def encode(message):
    message+=" "
    run_len=""
    count=0
    i=0
    for i in range(0,len(message)-1):
        
        if message[i]!=message[i+1]:
            count+=1
            run_len+=str(count)
            run_len+=message[i]
            count=0
        else:
            count+=1
             
       
    return run_len

encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)