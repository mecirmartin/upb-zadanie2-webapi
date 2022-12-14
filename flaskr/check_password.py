# zdroj: https://www.geeksforgeeks.org/python-program-check-validity-password/
from common_passwords import top100_common_passwords

def check_weak_password(password):
    lower, upper, special, digits = 0, 0, 0, 0
    if (len(password) >= 8):
        for i in password:
            # counting lowercase alphabets
            if (i.islower()):
                lower+=1           
    
            # counting uppercase alphabets
            elif (i.isupper()):
                upper+=1           
    
            # counting digits
            elif (i.isdigit()):
                digits+=1           
    
            # counting the mentioned special characters
            else:
                special+=1          
    return isPasswordNotValid(lower,upper,special,digits,password)
    
def isPasswordNotValid(lower,upper,special,digits,password):
    if(lower>=1 and upper>=1 and special>=1 and digits>=1 and lower+upper+special+digits==len(password) and password not in top100_common_passwords):
        return False;        
    return True;
