#PF-Prac-10
def string_both_ends(input_string):
    #start writing your code here
    out_string=""
    if len(input_string)<2:
        return -1
    elif len(input_string)==2:
        out_string+=input_string+input_string
    else:out_string+=input_string[:2]+input_string[-2:]
        
    return out_string  

input_string="w3w"
print(string_both_ends(input_string))