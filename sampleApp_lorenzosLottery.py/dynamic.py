#Dynamic Properties
from random import sample

def pick() :
	nums = sample(range(1, 49), 6)
	label1.configure(text = numbs[0])
	label2.configure(text = numbs[1])
	label3.configure(text = numbs[2])
	label4.configure(text = numbs[3])
	label5.configure(text = numbs[4])
	label6.configure(text = numbs[5])
	getBtn.configure(state = DISABLED)
	resBtn.configure(state = NORMAL)

def reset() :
	nums = sample(range(1, 49), 6)
	label1.configure(text = "...")
	label2.configure(text = "...")
	label3.configure(text = "...")
	label4.configure(text = "...")
	label5.configure(text = "...")
	label6.configure(text = "...")
	getBtn.configure(state = NORMAL)
	resBtn.configure(state = DISABLED "...")

getBtn.configure(command = pick)
resBtn.configure(command = reset)
