mydict={}
a = input("enter the no of names: ")
for i in range(int(a)):
	name = (input("enter name: "))
	if name not in mydict.keys():
		mydict[name] =1
	else:
		mydict[name] += 1
for name in mydict.keys():
	print(f"{name} --> {mydict[name]}")		

