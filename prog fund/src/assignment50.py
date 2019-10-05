#PF-Assgn-50

def sms_encoding(data):
    encode=data.split()
    code=""
    
    for el in encode:
        if el in ['a','e','i','o','u','A','E','I','O','U']:
            code+=el+" "
        elif el==" ":
            code+=el+" "
        
        else:
            
            con=""
            for i in range(len(el)):
                if el[i] not in ['a','e','i','o','u','A','E','I','O','U']:
                    con+=el[i]
            code+=con+" "
                    
    code=code[:-1]
    return code
data="I love Python"
print(sms_encoding(data))