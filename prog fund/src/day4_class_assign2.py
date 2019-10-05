dict1={778028:50000,778029:20000,778030:25000,778031:55000}
sum1=0
for key,value in dict1.items():
    sum1+=value
#var="SUM"    
dict1.update({"SUM":sum1})
print(dict1)
