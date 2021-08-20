temp = float(input("What is the temperature? "))
f_or_c = input("Farenheit or Celsius? (f or c)")
print()
a = 1
fahrenheit = temp
if f_or_c == "c":
	fahrenheit = (temp * 9/5) + 32
	f_or_c = "f"

a=0
wind = 5
windchill = 0
if f_or_c == "f":
	
	print()
	while a < 13:
		


		offset = 13.12
		factorone = 0.6215
		factortwo = -11.37   
		factorthree = 0.3965
		exp = 0.16
		wci = round(offset + (factorone * temp) + (factortwo * wind ** exp) + (factorthree * temp * wind ** exp), 2)


		
		print("At temperature ", fahrenheit , "F, and wind speed ", wind , " mph, the windchill is: ", wci , "F")
		wind += 5
		a =+1
		if wind >= 65:
			break
	
