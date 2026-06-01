# ---------------------here i use function-----------------------

def Resume_maker(name, age, cgpa, grade, is_passed, email, phone_number, address, course, university, branch, year_of_study, project_link, skills, Github_profile, LinkedIn_Profile):

   
    print("Name:", name)
    print("Age:", age)
    print("CGPA:", cgpa)
    print("Grade:", grade)
    print("1st Semester Result:", is_passed)
    print("Email:", email)
    print("Phone Number:", phone_number)
    print("Address:", address)
    print("Course:", course)
    print("University:", university)
    print("Branch:", branch)
    print("Year of Study:", year_of_study)
    print("Project Link:", project_link)
    print("Skills:", skills)
    print("GitHub Profile:", Github_profile)
    print("LinkedIn Profile:", LinkedIn_Profile)
    
# ---------------------here i use variables-----------------------

# Here i use input and output Statement
print("welcome to Internship program")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# ---------------here i use if else statement-------------
if age<=18:
    print("You are not eligible for this internship program")
    # ----------------Here i use break Statement-----------------
    exit()
cgpa = float(input("Enter your CGPA: "))
if cgpa<7.0:
    print("you are eligible for only 1 month intern program")
elif cgpa>=7.0 and cgpa<8.0:
    print("you are eligible for only 2 month intern program")
else:
    print("you are eligible for full time intern program")


grade = input("Enter your grade: ")
is_passed = bool(input("Enter your 1st semester result  (True = pass/ False = back): "))
if is_passed == False:
    print("You are not eligible for this internship program")
    exit()
email = input("Enter your email: ")
phone_number = int(input("Enter your phone number: "))
#   -----------------Here i use length of String-----------------
if(len(str(phone_number))!=10):
    print("Invalid phone number. Please enter a 10-digit phone number.")
    phone_number = (input("Enter your phone number: "))   
address = input("Enter your address: ")
course = input("Enter your course:(CSD, CSE) ")

#  -----------------Here i use logical operator-----------------
if(course!="CSD" and course!="CSE"):
    print("Invalid course. Please enter either 'CSD' or 'CSE'.")
    
    course = input("Enter your course:(CSD, CSE) ")


university = input("Enter your university: ")
branch = input("Enter your specialization: ")
year_of_study = int(input("Enter your year of study: "))
if year_of_study<1 or year_of_study>4:
    print("Invalid year of study. Please enter a value between 1 and 4.")
    year_of_study = (input("Enter your year of study: "))
project_link = input("Enter your project link: ")
skills = input("Enter your skills: ")
Github_profile = input("Enter your GitHub profile link: ")
LinkedIn_Profile = input("Enter your LinkedIn profile link: ")



print(Resume_maker(name, age, cgpa, grade, is_passed, email, phone_number, address, course, university, branch, year_of_study, project_link, skills, Github_profile, LinkedIn_Profile))
print("Thank you for applying to our internship program. We will review your application and get back to you soon.")