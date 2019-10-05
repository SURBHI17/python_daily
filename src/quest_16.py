#PF-Prac-16
def rotate_list(input_list,n):
    #start writing your code here
    output_list=input_list[:len(input_list)-n]
    rotate=input_list[len(input_list)-n:]
    
    output_list=rotate+output_list

    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)