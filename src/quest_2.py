#PF-Prac-2
def bracket_pattern(input_str):
    count=0
    if input_str[0]==")" or input_str[-1]=="(":
        return False
    else:
        for el in input_str:
            if el=="(":
                count+=1
            else:
                count-=1
        if count==0:
            return True
        else: return False
        
input_str="(())("
print(bracket_pattern(input_str))