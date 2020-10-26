import random
import time

list=['r','p','s']
print("Welcome to Rock-Paper-Scissors\n")
time.sleep(1)
print("r : rock\np : paper\ns : scissors\n")
time.sleep(1)
print("Start\n")
chances=int(input("Enter the number of chances you want : "))
i=1
uscore,cscore=0,0

while(i<=chances):
	computer_hand=random.choice(list)
	time.sleep(1)
	user_hand=input("\nEnter : ")
	time.sleep(1)
	if user_hand not in list:
		print("Wrong Input (Chance won't be counted)")
	else:
		if(user_hand=='r'):
			if(computer_hand=='s'):
				print("Computer : ",computer_hand)
				uscore+=1
				print("You won, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			elif(computer_hand=='p'):
				print("Computer : ",computer_hand)
				cscore+=1
				print("You lose, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			else:
				print("There's a tie!")
				print("Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
		elif(user_hand=='s'):
			if(computer_hand=='p'):
				print("Computer : ",computer_hand)
				uscore+=1
				print("You won, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			elif(computer_hand=='r'):
				print("Computer : ",computer_hand)
				cscore+=1
				print("You lose, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			else:
				print("There's a tie!")
				print("Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
		else:
			if(computer_hand=='r'):
				print("Computer : ",computer_hand)
				uscore+=1
				print("You won, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			elif(computer_hand=='s'):
				print("computer : ",computer_hand)
				cscore+=1
				print("You lose, Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))
			else:
				print("There's a tie!")
				print("Score :- \nComputer : {}\nYou :{}".format(cscore,uscore))

		print("\nTotal chances left : ",chances-i)
		i+=1

time.sleep(1)
print("Over. Final Scores :- \nComputer : {} \nYou : {} ".format(cscore,uscore))
time.sleep(1)

if(uscore<cscore):
	print("Computer Won !")
elif(uscore>cscore):
	print("You Won !")
else:
	print("Game tied !")