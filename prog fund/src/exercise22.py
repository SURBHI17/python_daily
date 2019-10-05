#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    count=101
    #while(no_of_passengers>0):
    for i in range(0,no_of_passengers):
        ticket_number_list.append(airline+":"+source[:3:]+":"+destination[:3:]+":"+str(count))
        count=count+1
    if len(ticket_number_list)>5:
        return ticket_number_list[-5::]
    #Write your logic here

    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
