courses = ["CHEM 1050","ENGI 1010", "ENGI 1020", "ENGI 1030", "ENGI 1040", "ENGL 1090", "MATH 1001", "MATH 2050", "PHYS 1051"]
grades = []

for course in courses:
    grade = int(input(f'Enter your {course} grade: '))
    while grade < 0:
        print("Please enter a valid score")
        grade = int(input(f'Enter your {course} grade: '))
    else:
        pass
        
    grades.append(grade)

average = (sum(grades)/len(grades))

mark_needed = 70

promotable = average >= mark_needed

if promotable == True:
    print(f"Congratulations!, your grade was {average}")
else: print("Not promotable")