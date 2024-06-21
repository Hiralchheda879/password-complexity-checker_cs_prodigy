name=(input("enter your name:"""))
print ("welcome"+" "+name)
import re
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    if criteria_met == 5:
        strength = 'Very Strong'
    elif criteria_met == 4:
        strength = 'Strong'
    elif criteria_met == 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'
   

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
         feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")
   
    return strength, feedback
password=(input("enter your password"))
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
for comment in feedback:
    print(comment)