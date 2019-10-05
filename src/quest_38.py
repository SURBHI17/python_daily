#PF-Prac-38
def build_index_grid(rows, columns):
    result_list=[]
    for i in range(rows):
        str1=""
        row=[]
        
        for j in range(columns):
            str1=str(i)+","+str(j)
            row.append(str1)
        result_list.append(row)
        

    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
   