#PF-Assgn-29
def calculate(distance,no_of_passengers):
    total_fare=0
    fuel_price=0
    profit=0
    #Remove pass and write your logic here
    mileage=10
    price_petrol=70
    ticket_price=80
    
    total_fare=no_of_passengers*ticket_price
    
    fuel_price=(distance/mileage)*price_petrol
    
    profit=total_fare-fuel_price
    if profit<0:
        return -1
    return profit



#Provide different values for distance, no_of_passenger and test your program
distance=5
no_of_passengers=10
print(calculate(distance,no_of_passengers))