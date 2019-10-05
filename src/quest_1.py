#PF-Prac-1
def add_string(str1):
    #start writing your code here
    if len(str1)>2:
        if str1[-3:]!="ing":
            str1+="ing"
        else:
            str1+="ly"
    return str1

str1="com"
print(add_string(str1))