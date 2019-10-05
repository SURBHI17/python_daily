#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    if(day<=29):
        if(month==2):
            if(day==28)and((year%4==0 and year%100!=0) or year%400==0):
                day+=1
            else:
                day=1
                month+=1
        else:
            day+=1        
                
            
    elif(day==30 or 31):
        if(month==1 or 3 or 5 or 7 or 8 or 10)and day==31 :
            day=1
            month+=1
        elif(month==4 or 6 or 9 or 11) and day==30:
            day=1
            month+=1
        else:
            day+=1
            
    else:
        day=1
        month=1
        year+=1   
  
        

    print(day,"-",month,"-",year)


generate_next_date(28,2,2016)