import tkinter as tk


def process(*args):
    val = ent_value.get()
    check = check01(val)
    
    if (check == True):
        val = remove0(val)
        output = base2to10(val)
        lab_output.config(text = str(val) + " --> " + str(output))
    
    else:
        lab_output.config(text = "Invalid")
    
    ent_value.delete(0,tk.END)



def base2to10(str):
	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
		total = total + int(str[i]) * 2**n
		n = n + 1

	return total


def remove0(str):
	for i in range(0, len(str),1):
		if (str[i] == "1"):
			return str[i:]

	return str


def check01(str):
	num_0 = str.count("0")
	num_1 = str.count("1")

	if num_0 + num_1 == len(str):
		return True
	return False






root = tk.Tk()

# Creates widgets
lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)
lab_output = tk.Label(root, text = "***")

# Configuration of widgets


# Places widgets in the window (root)
lab_instructions.pack()
ent_value.pack()
lab_output.pack()

root.bind("<Return>", process)
root.mainloop()
