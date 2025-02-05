# Initialize empty strings for personal information variables
name = ''    
age = ''
fav_color = ''


# First loop for gathering initial personal information
while True:    
     
    # Display welcome message and initial options
    welcome = print('''welcome! choose:    
1 - to enter your name         
2 - to enter your age         
3 - to enter you favorite color
4 - to display your personal info                    
5 - to continue         
''')
    
     # Create a dictionary with the current personal information
    personal_dic = {
'name' : name,
'age' : age,
'favorite color' : fav_color
}

    
    # Prompt the user for a menu choice
    choice = int(input('enter 1, 2, 3 or 4 for the corresponding menu choices: '))

    if choice == 1:
        name = input('enter your name: ')
        print(f"that's awesome {name}! nice meeting you")
    elif choice == 2:
       age = int(input('how old are you: '))
    elif choice == 3:
       fav_color = input('what is your favorite color: ')
       print(f"oooooh, {fav_color} is my favorite color too!!")
    elif choice == 4:
       print(personal_dic)
    elif choice == 5:
       break
    else:
       print('invalid choice')


# After collecting initial info, prompt for the names of friends
names_of_friends = input('enter the names of your friends. (names should be seperated by a comma(,)): ')

# Create a list by splitting the input string at each comma followed by a space
list_of_friends = names_of_friends.split(', ')


# Initialize variables for updated personal information with empty values
new_name = ''
new_age = ''
new_fav_color = ''


# Loop for updating personal information and friend list
while True:
   
   # Display update menu options
   print('''to make any updates, choose:
1 - to update name
2 - to update age
3 - to update favorite color
4 - to remove a friend from the list
5 - to display (updated) personal information
6 - to display (updated) list of friends
7 - to quit
''')
   
   
   # Create a dictionary with the updated personal information
   personal_dic = {
'name' : new_name,
'age' : new_age,
'favorite color' : new_fav_color
}

   
   # Prompt the user for a menu choice for updates
   choice = int(input('enter 1, 2, 3, 4, 5, 6 or 7 for the corresponding menu choices: '))

   if choice == 1:
      new_name = input('input new name: ')
      print(f'name has been updated to {new_name}')
   elif choice == 2:
      new_age = int(input('input new age: '))
      print(f'age has been updated to {new_age}')
   elif choice == 3:
      new_fav_color = input('input new favorite color: ')
      print(f'favorite color has been updated to {new_fav_color}')
   elif choice == 4:
      remove_friend = input(f'type in name of friend you want to remove from this list {list_of_friends}: ')
      if remove_friend in list_of_friends:
         list_of_friends.remove(remove_friend)
         print(f'{remove_friend} has been removed from the list.') 
   elif choice == 5:
      print(personal_dic)
   elif choice == 6:
      print(f'this is your new list of friends {list_of_friends}')
   elif choice == 7:
      break
   else:
      print('invalid choice')