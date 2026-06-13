import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
students_path = BASE_DIR / "students.json"

with open(students_path, "r") as f:
    students = json.load(f)

menu = """
    Menu:
    1. Add student   
    2. View students  
    3. Delete student  
    4. Update grade  
    5. Average grade  
    6. Highest grade  
    7. Lowest grade  
    8. Quit  
    """

while True:

    print(menu)
    option = input("Choose option: ")

    if option == "1":
        question1 = input("Enter student's name: ")
        question2 = input("Enter student's grade: ")

        found = False

        for student in students:
            if question1.lower() == student["Student"].lower():
                print("Student already exists")
                found = True
                break

        if not found:

          try:  
            grade = int(question2)

            if 0 <= grade <= 100:
                students.append({
                    "Student": question1,
                    "Grade": question2
                })  

                with open(students_path, "w") as f:
                    json.dump(students, f)
                
                print("Student added successfully")

            else:
                print("Grade must be between 0 and 100")
            
          except ValueError:
              print("Please enter a number.")

    elif option == "2":
        for i, student in enumerate(students, start=1):
           print(f"{i}. {student['Student']} - {student['Grade']}")

    elif option == "3":
        student_num = int(input("Enter student number to delete: "))
        
        if 1 <= student_num <= len(students):
            del students[student_num - 1]

            with open(students_path, "w") as f:
                json.dump(students, f)
        
        else:
            print("Invalid student number")

    elif option == "4":
        student_num = int(input("Enter student number to update: "))
        new_grade = input("Enter new grade: ")

        grade = int(new_grade)
        if 0 <= grade <= 100:
            students[student_num - 1]["Grade"] = grade

            with open(students_path, "w") as f:
                json.dump(students, f)
        
        else:
            print("Grade must be between 0 and 100")

    elif option == "5":
         if len(students) == 0:
             print("No students found.")
        
         else:
             total = 0
             
             for student in students:
                 total += int(student["Grade"])
                 
             average = total / len(students)
             print(f"Average grade: {average:.2f}")

    elif option == "6":
        if len(students) == 0:
            print("Invalid number.")

        else:
            highest = students[0]
            
            for student in students:
                if int(student["Grade"]) > int(highest["Grade"]):
                    highest = student
            
            print(f"Highest grade: {highest['Student']} - {highest['Grade']}")

    elif option == "7":
        if len(students) == 0:
            print("Invalid number.")

        else:
            lowest = students[0]
            
            for student in students:
                if int(student["Grade"]) < int(lowest["Grade"]):
                    lowest = student
                    
            print(f"Lowest grade: {lowest['Student']} - {lowest['Grade']}")
         
    elif option == "8":
        print("Goodbye!")
        break

    



