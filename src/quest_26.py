#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    string=string.lower()
    if string.count("mat")==string.count("jet"):
        return True
    return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))