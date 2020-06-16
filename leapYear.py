def checkYear(year): 
	import calendar 
	return(calendar.isleap(year)) 
	 
year = int(input("Enter a Year"))
if (checkYear(year)): 
	print("Leap Year") 
else: 
	print("Not a Leap Year") 
		
# This code is contributed by Chin 

