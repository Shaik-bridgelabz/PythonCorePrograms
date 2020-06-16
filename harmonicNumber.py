# Python3 program to find 
# N-th Harmonic Number 

# Function to find N-th Harmonic Number 
def nthHarmonic(N) :
	harmonic = 1.00
	for i in range(2, N + 1) : 
		harmonic += 1 / i 
	return harmonic

#Taking user Input
num=int(input("Enter the number: "))

#Ensure num !=0
if (num != 0):
	print(round(nthHarmonic(num),5))
else:
	print("Number cannot be zero")
