'''
Lab5
'''

#3.1

alien_color = 'red'

if alien_color == "green":
    print('you have earned 5 points')
    
#3.2
alien_color = 'yellow'

if alien_color == "green":
    print('you have earned 5 points')

else:
    print('you have earned 10 points')
    
#3.3

favoriate_fruits = ['apple', 'banana', 'orange']

if 'mango' in favoriate_fruits:
    print('you really like mango')
    
if 'apple' in favoriate_fruits:
    print('you really like apple')
    
if 'orange' in favoriate_fruits:
    print('you really like orange')
    
#3.4

age = 20

if age<10:
    print('kid')
elif age >=10 and age <20:
    print('teenager')
else:
    print('adult')
    if age >=65:
        print('elder')