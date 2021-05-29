print("You started a new game! Congratulations!")
print()
print("You have just had a very important phone call with a potential employer.")
print("You have been in search of a new job that would treat you better than you had been at your last place of emplyement.")
print("John, the employer, asked you to submit to him your desired salary by 5pm today.")
print()
salary = int(input("What salary do you with to obtain in this job? "))
print()
print("Some time later...")
print("Thank you for submiting your desired wages! I see that you are looking for", salary,"dollars. ")
print()




if salary > 75000:
	print("We reviewed the slary that you presented and are sorry that we cannot provide that amount for you.")
	print("However we would like to offer you 6500. Would you be interested in this amount?")
	high_salary = input("YES or NO: ")
	if high_salary == "yes":
		print("Great, We look forward to working with you! We have just sent you an email with a document you need to sign before you come into work on monday.")
	elif high_salary == "no":
		print("You said no")
		
		
		
		
elif salary >= 45001:
	print("Good news! We have accepted your request for,", salary, "!")
	print("We will send you an email with a document to sign before you start work on monday.")
	
	
	
elif salary <= 45000:
	print("Are you sure you don't want to ask for more than,", salary,"?")
	low_salary = input("YES or NO: ")
	if low_salary == "yes":
		print("Upon reviewing your request, we have determined that we will offer you the job, at out starting salary for this position.")
		print("You will recieve an email shortly. Please sign the document, which will indicate that you accept the job position.")
	elif low_salary == "no":
		salary = int(input("What salary do you with to obtain in this job? "))
		
		
		
		
		
else:
	print("TRY AGAIN")
