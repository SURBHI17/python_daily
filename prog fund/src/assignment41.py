#PF-Assgn-41
def find_ten_substring(num_str):
    ten_list=[]
    for i in range(len(num_str)):
        if num_str[i]=="0":
            continue
        sum=0
        for j in range(i,len(num_str)):
            sum+=int(num_str[j])
            if sum==10:
                ten_list.append(num_str[i:j+1])
    return ten_list


#through recursion

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)