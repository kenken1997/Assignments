
def add_student(students, name, age, grade):
   
    student = {'name': name, 'age': age, 'grade': grade}
   
    students.append(student)
    print(f'Student {name} added successfully.\n')


def update_student(students, name, new_age, new_grade):
 
    for student in students:
        if student['name'] == name:
          
            student['age'] = new_age
            student['grade'] = new_grade
            print(f'Student {name} updated successfully.\n')
            return  
   
    print(f'Student {name} not found.\n')

def display_students(students):
    if not students:
        print('No student records available.\n')
        return
    print('Student Records:')
    
    for student in students:
        print(f'Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}')
    print('') 


def calculate_average_grade(students):
    if not students:
        print('No student records available to calculate average grade.\n')
        return
   
    total = sum(student['grade'] for student in students)
    
    average = total / len(students)
    print(f'Average grade of all students: {average:.2f}\n')
    return average


def main():
  
    students = []
    

    while True:
        print('''Student Records Management System
1. Add new student
2. Update existing student record
3. Calculate average grade of all students
4. Display all student records
5. Exit''')
        
      
        choice = input("Enter your choice (1-5): ")
        print('')
       
        if choice == '1':
            name = input("Enter student's name: ").title()
            while True:
                try:
                    age = int(input("Enter student's age: "))
                    break
                except ValueError:
                    print('Age can only be an integer. \n')
            while True:
                try:
                    grade = float(input("Enter student's grade: "))
                    break
                except ValueError:
                    print('Invalid input. Grade can only be decimal \n')

            add_student(students, name, age, grade)
        
        elif choice == '2':
            name = input("Enter the name of the student to update: ").title()
            while True:
                try:
                    new_age = int(input("Enter new age: "))
                    break
                except ValueError:
                    print('Age can only be an integer. \n')
            while True:
                try: 
                    new_grade = float(input("Enter new grade: "))
                    break
                except ValueError:
                      print('Invalid input. Grade can only be decimal \n')

            update_student(students, name, new_age, new_grade)
        
        elif choice == '3':
            calculate_average_grade(students)
        
        elif choice == '4':
            display_students(students)
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again. \n")


if __name__ == "__main__":
    main()



