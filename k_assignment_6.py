data = []
    
while True:

    print('Welcome to the Student Management System')

    print('''Choose an option
1. Add a student, collect(name, age, grade and a list of courses)
2. Remove a Student
3. View all Students
4. Exit''')
     
     
    choice = input('Enter your choice: ')

    if choice == '1':
        s_name = input('Enter student name: ').title()
        s_age = int(input('Enter student age: '))
        s_grade = input('Enter student grade: ').title()
        s_course = input('Enter student course: ').title()
        print(f'{s_name} has been added to the system')

    
        student = {
        'name': s_name,
        'age': s_age,
        'grade': s_grade,
        'course': s_course
    }
        data.append(student)


    elif choice == '2':
        rem_student = input('Enter student name to remove: ').title()
    found = False  
    for student in data:
        if student['name'] == rem_student:
            data.remove(student)  
            print(f'{rem_student} has been removed from the system')
            found = True
            break  
    if not found:
        print(f'{rem_student} not found in the system')


    elif choice == '3':
      print('Students in the system ')
      for student in data:
        print(student)

    elif choice == '4': 
     print('Goodbye')
     break

    else:
       print('Invalid entry')