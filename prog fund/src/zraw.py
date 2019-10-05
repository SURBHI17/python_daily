#PF-Tryout
def generate_schedule(module_list,duration_list,start_date):   
    #start writing your code here
    end_date=""
    month_key={1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
    day_list={1:"sun",2:"mon",3:"tue",4:"wed",5:"thu",6:"fri",0:"sat"}
    year_key=6
    date=start_date.split("-")
    year=int(date[-1][-2:])
    year1=date[-1]
    date1=int(date[0])
    month=int(date[1])
    r=(year//4)+date1+month_key[month]+year_key+year
    if month==1 or 2:
        r=r-1
    r=r%7
    day=day_list[r]
    for i in range(len(module_list)):
        if duration_list[i]>10:
            return -1
        elif duration_list[i]<6:
            date1=date1+duration_list[i]
            end_date=str(date1)+"-"+str(month)+"-"+year1
        else:
            date1=date1+duration_list[i]+1
            end_date=str(date1)+"-"+str(month)+"-"+year1
        print(module_list[i],"-","start_date: ",start_date," End_date: ",end_date)        
        date1+=1
        start_date=str(date1)+"-"+str(month)+"-"+year1
    return       

module_list=["PF","OOP"]
duration_list=[7,8]
start_date="01-03-2016"
generate_schedule(module_list, duration_list, start_date)