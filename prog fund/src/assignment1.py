#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    if(job_level==3):new_salary=1.15*current_salary
    elif(job_level==4):new_salary=1.07*current_salary
    elif(job_level==5):new_salary=1.05*current_salary
    else:
        new_salary=current_salary

    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)