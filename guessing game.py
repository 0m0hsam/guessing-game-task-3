import random
import sys

scores=0
play=0
print(f'Welcome to Guessing game')
print(f'Design by incredible Sam and Start.ng')
print(f'Do you think you can guess right play, let see....')
print(f'To play level 1 enter EASY')
print(f'To play level 2 enter MEDIUM')
print(f'To play level 3 enter HARD')
try:
	level=(input('Enter the game level you want to play: ' )).upper()
except ValueError:
	print(f"Wrong entry! please check")
	sys.exit()
if level == "EASY":
	counter=10
	print(f'Welcome to level 1')
	print(f'Your have {counter} guessing power')
	
	while play < 10 :
		try:
			guess =int(input("guess a number:   "))
		except ValueError:
			print(f"Wrong entry! guess only number try again")
			sys.exit()
		rand=random.randint(1,2)
		play += 1
		counter -=1
		
		if rand == guess :
			print(f'You guess right')
			print(f'Your guessing power remain : {counter}')	
			scores+=1
			
			if scores == 6:
				print('You won!')
				print('Level one completed')
				break
		else :
			print(f'That guess was wrong')
			print(f'Your guessing  power remain : {counter}')
	
	print(f'Game Over!')
	print(f'You guess {scores} right out of 10')

elif level == "MEDIUM":
	print(f'Welcome to level 2')
	counter = 20
	print(f'Your have {counter} guessing power')
	
	while play < 20 :
		try:
			guess = int(input("guess a number:   "))
		except ValueError:
			print(f"Wrong entry! guess only number try again")
			sys.exit()
		rand=random.randint(1,10)
		play += 1
		counter -=1
		
		if rand == guess :
			print(f'You guess right')
			print(f'Your guessing power remain : {counter}')	
			scores+=1
			
			if scores == 4:
				print('You won!')
				print('Level two completed')
				break
		else :
			print(f'That guess was wrong')
			print(f'Your guessing  power remain : {counter}')
	
	print(f'Game Over!')	
	print(f'You guess {scores} right out of 20')

elif level == "HARD":
	print(f'Welcome to level 3' )
	counter = 50
	print(f'Your have {counter} guessing power')
	
	while play < 50 :
		try:
			guess = int(input("guess a number:   "))
		except ValueError:
			print(f"Wrong entry! guess only number try again")
			sys.exit()
		rand=random.randint(1,15)
		play += 1
		counter -=1
		
		if rand == guess :
			print(f'You guess right')
			print(f'Your guessing power remain : {counter}')	
			scores+=1
			
			if scores == 3:
				print('You won!')
				print('Level Three completed')
				break
		else :
			print(f'That guess was wrong')
			print(f'Your guessing  power remain : {counter}')
			
	print(f'Game Over!')	
	print(f'You guess {scores} right out of 50')
else:
	print(f'Oops! you entered a wrong level')



	