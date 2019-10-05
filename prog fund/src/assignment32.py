#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count_p=0
    count_e=0
    count_o=0
    max1=0
    i=0
    l=len(patient_medical_speciality_list)
    while(l>0):
        if(patient_medical_speciality_list[i]=="P"):
            count_p+=1
        elif(patient_medical_speciality_list[i]=="O"):
            count_o+=1
        elif(patient_medical_speciality_list[i]=="E"):
            count_e+=1
        i+=1
        l-=1
   
    max1=max(max(count_e,count_o),max(count_o,count_p))
    if(max1==count_e):speciality=medical_speciality["E"]
    elif(max1==count_o):speciality=medical_speciality["O"]
    else:speciality=medical_speciality["P"]
    
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)