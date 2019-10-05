#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    win1=0
    win2=0
    for el in match_tuple:
        if el=="Team1": 
            win1+=1
        else:
            win2+=win1
    if win1==max(win1,win2):
        return "Team1"
    elif win1==win2:
        return "Tie"
    else:
        return "Team2"
#Invoke the function with each of the print statements given below
#print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
