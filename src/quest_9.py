#PF-Prac-9
def generate_dict(number):
    #start writing your code here
    new_dict={}
    i=1
    while(i<=number):
        new_dict.update({i:i*i})
        i+=1

    return new_dict

number=20
print(generate_dict(number))