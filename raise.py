day = 32
try :
	if day > 31 :
		raise ValueError("Invalid Day Number")
except ValueError as message :
	print("The Program found An", message)
finally :
	print("Don't Worry, It happens to the best of us")

