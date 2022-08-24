import random

top_of_range = eval(input('type a number '))




if top_of_range <= 0:
  print('please a enter a number greater than 0')
  quit()

random_number = random.randint(0,top_of_range)
print(random_number)
guess = 0
while True:
  guess += 1
  user_guess = eval(input('make a guess '))
  
  
  
  
  if user_guess == random_number:
    
    print('u got it right')
    break
  else:
    if user_guess > random_number:
      print('you were above the number')
    
    else:
      print('you were below the number')
  
      
    
   
      
    
  
print('you got', guess, 'guesses')