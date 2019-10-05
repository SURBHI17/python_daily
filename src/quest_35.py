#PF-Prac-35
def convert_to_roman(num):
    #Start writing your code here
    str1=""
    dict={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    if num in dict:
        return dict[num]
    elif num<9:
        if num<4:
            while num>0:
                str1+= dict[1]
                num-=1
            return str1
        elif num==4:
            return dict[1]+dict[5]
        else:
            count=num-5
            while(count>0):
                str1+= dict[1]
                count-=1
                
            return dict[5]+str1
    
            
        
                
                
num=8
print(convert_to_roman(num))   
 
 
# for num in range(1,5000):    
#     print(num," : ",convert_to_roman(num))