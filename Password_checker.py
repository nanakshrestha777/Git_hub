#passwordchecker
password = input("Enter your Password to check: ")

def password_checker(password):
    
     # Initialize variables to keep track of password strength
    length = False
    digits = False
    uppercase = False
    lowercase = False
    message = ""
    
       # Check password length
    if  len(password) >= 8:
        length = True

         
    # Check for digits
    for c in password:
        if c.isdigit():
            digits = True
            break
     # Check for uppercase characters
    for c in password:
        if c.isupper():
            uppercase = True
            break
  # Check for lowercase characters
    for c in password:
        if c.islower():
            lowercase = True
            break

              # Generate password strength message
    if length and digits and uppercase and lowercase:
        message = "Your password is strong."
        
    else:
        if not length:
            message +=  "\n _Required 8 letters"
                
        if not digits:
            message += "\n _Required digits"
            
        if not uppercase:
            message += "\n _Required uppercase"
            
        if not lowercase:
            message += "\n _Required lowercase"            
        
    return message

strength = password_checker(password)
print(strength)
        
        
            
    
        
