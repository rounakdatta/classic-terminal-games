import getpass

from random import randint
player=input('You : rock(r), paper(p), scissor(s) : ')
if(player=='r' or player=='p' or player=='s'):
	print(player, 'vs ', end='')
	comp=randint(1,3)
	if(comp==1):
		comp='r'
	elif(comp==2):
		comp='p'
	elif(comp==3):
		comp='s'
	else:
		print('huh?')
	print(comp)
	if(player==comp):
		print("DRAW!")
	else:
		if((comp=='r' and player=='s') or (comp=='p' and player=='r') or (comp=='s' and player=='p')):
			print("Computer wins!")
		else:
			print(getpass.getuser().capitalize(),"wins!")
else:
	print("Foul play!")