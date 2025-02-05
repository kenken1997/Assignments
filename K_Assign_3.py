User_Sentence = input("Write any sentence you want: ")   #prompt asking user for their input

print(f'total number of characters including spaces is {len(User_Sentence)}')   #displays total number of characters user inputs

print(f'total number of words in the sentence is {len(User_Sentence.split())}')   #displays total number of words user inputs

words = User_Sentence.split()   #splits the input sentence into seperate units
first_word = words[0]   #returns first word of sentence
last_word = words[-1]   #retuns last word of sentence

print(f'first word is: {first_word}')    #displays first word of input sentence
print(f'last word is: {last_word}')     #displays last word of input sentence

print(f'first three characters of the sentence are: {User_Sentence[:3]}')    #displays first three characters of input sentence

print(f'last three characters of the sentence are: {User_Sentence[-3:]}')    #displays last three characters of input sentence

print(f'sentence in reverse order is: {User_Sentence[::-1]}')   #displays input sentence in reverse order

UpperC = User_Sentence.upper()    #returns input sentence to uppercase
LowerC = User_Sentence.lower()    #returns input sentence to lowercase

print(f'sentence in upper case is: {UpperC}')     #displays input sentence in uppercase
print(f'sentence in lowercase is: {LowerC}')     #displays input sentence in lower case

hypens = User_Sentence.replace(" ", "-")     #replaces all spaces in the sentence with hyphens
print(f'all spaces in the sentence replaced by hyphens: {hypens}')      #displays sentence with spaces replaced by hyphens
