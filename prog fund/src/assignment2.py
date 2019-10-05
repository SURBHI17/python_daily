#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    equivalent=0
    #write your logic here
    if(current_currency_name=="Euro"): equivalent=0.01417
    elif(current_currency_name=="British Pond"): equivalent=0.0100
    elif(current_currency_name=="Australian Dollar"):equivalent=0.02140
    elif(current_currency_name=="Canadian Dollar"):equivalent=0.02027
    else:
        print("Invalid currency name")
    current_currency_amount=amount_needed_inr*equivalent
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"British Pond")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")