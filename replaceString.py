userName = input ("Enter your Name: ")
str="Hello <<UserName>>,How are you?"
str2=str.replace("<<UserName>>",userName);

if(len(userName)<3):
	print("Name must be min 3 chracters")
else:
	print(str2)
