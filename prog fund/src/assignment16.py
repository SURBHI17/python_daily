#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    q=rupees_to_make//5
    r=rupees_to_make%5
    #Start writing your code here
    #Populate the variables: five_needed and one_needed
     
   
   
    if(5*no_of_five+no_of_one>=rupees_to_make):
        if(q<=no_of_five and r<=no_of_one ):
            five_needed=q
            one_needed=r
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        elif(r<=no_of_one):
            five_needed=no_of_five
            one_needed=rupees_to_make-5*five_needed
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
        
    else:
        print(-1)
        
make_amount(28,8,5)