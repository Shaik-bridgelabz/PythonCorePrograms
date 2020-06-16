limit = input("Upto how many terms to print power of 2? ")
term = int(limit);
if(0<=term<31):
	for i in range(0,term):
		res=(2**i);
		print("2 raised to the power",i,"=",res);
else:
	print("Number must be between 0 to 31")
