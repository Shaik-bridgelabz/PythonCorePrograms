import random
flips=int(input("Number of Times To Flip Coin: "))
heads=0;
tails=0;
if(flips >= 0):
	for i in range (0,flips):
		randomNumber=random.random()
		if(randomNumber>0.5):
			print("heads")
			heads=heads+1;
		else:
			print("tails")
			tails=tails+1;
	perHeads=int((heads*100)/flips);
	perTails=int(100-perHeads);
	print("Percentage of Heads is",perHeads)
	print("Percentage of Tails is ",perTails)
else:
	print("Number should be greater than zero")
