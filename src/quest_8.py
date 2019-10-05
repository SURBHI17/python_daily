#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount=0
    for el in trans_list:
        t=el[:1]
        value=el[2:]
        
        if t=="D":
            net_amount+=int(value)
        elif t=="W":
            net_amount-=int(value)
    
    return net_amount

#trans_list=["D:300","D:200","W:200","D:100"]
trans_list=['D:1300', 'D:350', 'W:1200', 'D:100']
print(calculate_net_amount(trans_list))