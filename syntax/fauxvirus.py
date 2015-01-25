#This is jsut me trolling and practicing what I have learned so far about Python 
import time

print("Welcome to Lorenzo's program.")
time.sleep(1)
print("\n\nMy name is Push")

time.sleep(1)
username = input("\n\nWhat is your name? ")
print("\n\nNice to meet you", username)
time.sleep(1)
print("\nLet's get to know each other a little more")

time.sleep(1)
age = input("\n\nHow old are you? ")
if int(age) > 50 or int(age) == 50:
	print("Damn you are old!")
elif int(age) < 18 or int(age) == 18:
	print("A young one I see!")
else:
	print("Wonderful, you still have a whole lot of years ahead of you XD")

time.sleep(1)
gender = input("\n\nWould you identify yourself as Male, Female or Other? ")
if gender == "male" or gender == "Male":
	print("Gotcha! We have a bro in the house")
elif gender == "female" or gender == "Female":
	print("Gotcha! We have a lady in the house")
elif gender == "other" or gender == "Other":
	print("Don't worry, we at Push don't hate on anybody")
else:
	input("Could you please try to enter an answer out of the options above?") 
	if input == "yes" or input == "yea" or input == "Yes" or input == "Yea":
		print("Good")
	elif input == "no" or input == "No":
		print("Well, FUCK YOU then!")
	else:
		print("You really can't follow simple directions, can you.....moron")

time.sleep(1)
print("\n\nNow the real fun begins :)")
time.sleep(1.5)
print("\nWhile you were answering these questions")
time.sleep(1.5)
print("\nWithout you noticing")
time.sleep(1.5)
print("\nI started hacking into your computer")
time.sleep(1.5)
print("\nYeaaaa")
time.sleep(1.5)
print("\nYou are FUCKED!")
time.sleep(3)
print("JK")
time.sleep(1.5)
print("I am just trolling")


