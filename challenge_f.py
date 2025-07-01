# declare the dictionaries
student_profile = {}
enrolled_input = {}

# Gets user input and assigns to dictionary
student_profile["name"] = input("Enter the student's name: ")
student_profile["year level"] = int(input("Enter the student year level (7, 8, 9, 10 ,11 or 12): "))
student_profile["grade"] = input("Enter the student grade (A, B, C, D, E or F): ")
student_profile["age"] = int(input("Enter the student's age: "))
student_profile["enrolled"] = input("Is the student enrolled? (Yes or No?) : ")

if student_profile["enrolled"] == "Yes":
    student_profile["enrolled"] = True
else:
    student_profile["enrolled"] = False


# Displays the profile
print("~Student Profile~")
print(f"Name: {student_profile['name']}")
print(f"Year Level: {student_profile['year level']}")
print(f"Grade: {student_profile['grade']}")
print(f"Age: {student_profile['age']}")
print(f"Enrolled: {student_profile['enrolled']}")

if student_profile["enrolled"] == True:
    print("Student is currently enrolled.")
else:
   print("Student is not currently enrolled.")









