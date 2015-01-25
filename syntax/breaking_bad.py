import time

print("Who would you like to meet?")
time.sleep(0.75)
print("\nJesse Pinkman")
time.sleep(0.5)
print("\nor")
time.sleep(0.5)
answer = input("\nWalter White? :")

if answer == "jesse" or answer == "Jesse" or answer == "Pinkman" or answer == "jesse Pinkman" or answer == "Jesse Pinkman" or answer == "jesse pinkman":
	import pinkman.py
	print(pinkman.py)
elif answer == "walt" or answer == "walter" or answer == "Walt" or answer =="Walter" or answer == "walter white" or answer == "Walter White":
	import heisenberg.py
	print(heisenberg.py)
else: 
	print("Seriously??")
	time.sleep(1)
	print("You do not watch the show?")
	time.sleep(1)
	print("Wow...")
	time.sleep(1)
	while (True):
		print(".")
		time.sleep(0.6)
		print(".")
		time.sleep(0.6)
		print(".")
		time.sleep(0.6)
		print("Wow...")
		time.sleep(1)
