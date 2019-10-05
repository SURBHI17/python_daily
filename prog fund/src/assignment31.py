#PF-Assgn-31
def check_palindrome(word):
    reverse=""
    reverse=word[::-1]
    if(word==reverse):
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")