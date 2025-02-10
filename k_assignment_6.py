#initializing a list
data = []

#initializing loop    
while True:
    
    #welcome message
    print('Welcome to the Student Management System')

    print('''Choose an option
1. Add a student, collect(name, age, grade and a list of courses)
2. Remove a Student
3. View all Students
4. Exit''')
     
    #prompt to ask user for their input choice 
    choice = input('Enter your choice: ')

    #if user enters '1', add student + their details
    if choice == '1':
        s_name = input('Enter student name: ').title()
        s_age = input('Enter student age: ')
        s_grade = input('Enter student grade: ').title()
        s_course = input('Enter student course: ').title()
        print(f'{s_name} has been added to the system')

    #add all details entered into 'student' dictionary
        student = {
        'name': s_name,
        'age': s_age,
        'grade': s_grade,
        'course': s_course
    }
    #append student dictionary into 'data' list 
        data.append(student)

    #if user enters "2", remove a stduent
    elif choice == '2':
        rem_student = input('Enter student name to remove: ').title()
    #initializes flag as False, meaning student has not been found yet
        found = False  
        for student in data:         #loops through the data list for 'student'
          if student['name'] == rem_student:      #if user input matches a value for name key in student dictionary, delete said dictionary
            data.remove(student)  
            print(f'{rem_student} has been removed from the system')
            found = True       #sets found to true if a match is found
            break            #breaks out of loop
    #if after looping, no value matched, print 'student not found'
        if not found:
          print(f'{rem_student} not found in the system')

    #if user enters "3", print all student dictionaries in data list
    elif choice == '3':
      print('Students in the system ')
      for student in data:
        print(student)

    #if user enters "4", break out of loop
    elif choice == '4': 
     print('Goodbye')
     break
    
    #error handling for if user enters any other value apart from 1, 2, 3 or 4
    else:
       print('Invalid entry')