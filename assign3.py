#had to write a code to check to see if someone is going to pass eng1

#listing the courses needed
courses = ["CHEM 1050","ENGI 1010", "ENGI 1020", "ENGI 1030", "ENGI 1040", "ENGL 1090", "MATH 1001", "MATH 2050", "PHYS 1051"]
grades = []

#getting them to input their grades
for course in courses:
    grade = int(input(f'Enter your {course} grade: '))
    while grade < 0:
        print("Please enter a valid score")
        grade = int(input(f'Enter your {course} grade: '))
    else:
        pass
        
    grades.append(grade)

#finding their average
average = (sum(grades)/len(grades))

mark_needed = 70

#seeing if they can promot
promotable = average >= mark_needed

if promotable == True:
    print(f"Congratulations!, your grade was {average}")
else: print("Not promotable")