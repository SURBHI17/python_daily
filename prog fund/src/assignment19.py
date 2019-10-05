#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    delivery_charges=0
    if(distance_in_kms<=3): 
        delivery_charges=0
    elif(distance_in_kms>3 and distance_in_kms<=6):
        delivery_charges=(distance_in_kms-3)*3
    else:
        delivery_charges=3*3+(distance_in_kms-6)*6
    
    #write your logic here
    if(food_type=="V" and quantity_ordered>0 and distance_in_kms>0):
        bill_amount=120*quantity_ordered+delivery_charges
    
    elif(food_type=="N" and quantity_ordered>0 and distance_in_kms>0):
        bill_amount=150*quantity_ordered+delivery_charges
    else:
        bill_amount=-1
    return bill_amount


bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)