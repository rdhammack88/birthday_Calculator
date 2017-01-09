
name = input('Please tell me your name: ')

print('Welcome ', name, '!',  'I will help you determine if today is your birthday.')
print()
#age = input('How old are you?')

todayMonth = input('What month is it? ')
todayDate = input('What is todays date? ')
todayYear = input('What is the current year? ')

print()

birthMonth = input('What month were you born in? ')
birthDate = input('What day were you born on? ')
birthYear = input('What year were you born in? ')

print()

currentAge = int(todayYear) - int(birthYear)

print('You are currently ', currentAge, ' years old.')
print()

if(birthMonth == todayMonth and todayDate == birthDate):
    print('Happy Birthday to you!')
elif(birthMonth == todayMonth and todayDate != birthDate):
    print('Not much longer!')
else:
    print('Still got a ways to go buddy!')
#(birthMonth != todayMonth and todayDate != birthDate)
print()
print(input('Press Enter to exit program'))

