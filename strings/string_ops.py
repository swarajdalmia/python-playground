
def case_change():
	name = "ada lovelace"
	# changes the string to title case, i.e. first letter of each word is caps
	print(name.title())
	# all in upper and lower
	print(name.upper())
	print(name.lower()) # makes sense to store data in lower case, and then display then in the style you'd want, irrespective of what the user has inputted. 
	
def concatenate():
	first_name = "ada"
	last_name = "lovelace"
	# strings are concatenated through "+"	
	print(first_name.title()+" "+last_name.title())

def white_spaces():
	# newline is added by \n and tab by \t
	print("adding tabs\tworks with escape\ncharacter even in quotes")
	# removes the extra spaces on the right 
	# if var.rstrip() is used, the right spaces will permanently be removed from the variable
	print("are there spaces left   ".rstrip()+".")
	# using var.lstrip() and var.strip() removes the empty spaces from both the left and the right

def length():
	# strings can be accessed using [] index. and len(s) gives the length of a string
	name = "Ada Lovelace"
	print(name[1])
	print(len(name))

