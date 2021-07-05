grade = int(input("What percent do you have in this class?"))

if grade >= 90:
	letter = "A"
elif grade >= 80:
	letter = "B"
elif grade >= 70:
	letter = "C"
elif grade >= 60:
	letter = "D"
else:
	letter = "F"
	
print(f"Your letter grade is a(n) {letter}")

