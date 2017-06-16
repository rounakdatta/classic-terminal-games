import random
mydict="dict.txt"

def hangman(f):
	print("\n\n\t\t___")
	init=['|','0','|','/','|','\\','/','\\']
	print("\t\t",init[0])
	print("\t\t",init[1])
	print("\t\t",init[2])
	if(f<5):
		print("\t\t\b\b ",init[3],end="")
	if(f<4):
		print(init[4],end="")
	if(f<3):
		print(init[5])
	if(f<2):
		print("\t\t\b",init[6],end="")
	if(f==0):
		print("",init[7])
		print("\n\n\t\t\t\t\tHANGMAN!\n\t\t\t\t\tYou lose!")
	print("\n\n\t\t----------------------------------------")

def run(word,compbox,chbox,chance):
	print("\n\t\tYour word:  ",end="")
	for j in range(0,len(word)):
		print(compbox[j]," ",end="")
	print("\n\n\t\tYour choice:  ",end="")
	print(chbox)
	print("\n\t\t---",chance," chance(s) remaining ---")
	hangman(chance)
	print("\n\n")

	pos=int(input("\t\tEnter position (start from 1): "))
	ch=input("\t\tEnter character: ")

	compbox = ''.join(compbox)

	if(ch==word[pos-1]):
		print("\n\t\t\t\tCorrect!")
		compbox=compbox[:(pos-1)]+ch+compbox[(pos):]
		chbox.remove(ch)
	else:
		print("\n\t\t\t\tWrong!")
		chance-=1

	if(compbox==word):
		print("\n\n\t\t\tDone! HANGMAN is saved!")
	else:
		if(chance>0):
			run(word,compbox,chbox,chance)
		else:
			hangman(chance)
			print("\t\t\t\tCorrect word was \"",word,"\"")

def start():
	print("\n\n\t\t\tWELCOME TO HANGMAN!\n\n")
	fx=open(mydict,'r')
	word=random.choice(fx.readline().split())

	print("\n\t\tYour word:  ",end="")
	c=0
	chbox=[]
	compbox=[]
	for i in range(0,len(word)):
		if(c<=1):
			if(random.choice([0,1])==1):
				print (word[i]," ",end="")
				c+=1
				compbox.append(word[i])
			else:
				print("_  ",end="")
				chbox.append(word[i])
				compbox.append("_")
		else:
			print("_  ",end="")
			chbox.append(word[i])
			compbox.append("_")

	random.shuffle(chbox)
	print("\n\n\t\tYour choice:  ",end="")
	print(chbox)

	print("\n\t\t---",(len(word)-c)," chance(s) remaining ---")
	hangman(len(word)-c)
	chance=len(word)-c
	print("\n\n")

	pos=int(input("\t\tEnter position (start from 1): "))
	ch=input("\t\tEnter character: ")
	if((pos in range(1,len(word))) and (ch in chbox)):
		compbox = ''.join(compbox)

		if(ch==word[pos-1]):
			print("\n\n\t\tCorrect!")
			compbox=compbox[:(pos-1)]+ch+compbox[(pos):]
			chbox.remove(ch)
		else:
			chance-=1

		run(word,compbox,chbox,chance)

	else:
		print("\n\n\t\t\tINVALID INPUT! TRY AGAIN!")
		start()

start()
print("\n\n")