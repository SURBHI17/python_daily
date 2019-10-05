#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years=[]
    i=given_year
    count=0
    while(count<15):
        
        if(i%4==0 and i%100!=0)or i%400==0:
            list_of_leap_years.append(i)
            i+=4
            count+=1
        else:
            i+=1
        
    # Write your logic here

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)