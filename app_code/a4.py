# Python library for connecting to Postgres servers
import psycopg2

# Establishing connection to the specified database
connector = psycopg2.connect(database="a4",user="postgres",password="postgrespassword",host="localhost",port='5432')

# Creating cursor object to run queries
c_obj = connector.cursor()

# Gets all the records from the 'students' relation
def getAllStudents():

	c_obj.execute("SELECT * FROM students")

	# The value stored in this variable holds the output of the previously executed query
	output = c_obj.fetchall()

	# Printing to display the data
	print(output)

# Adds a student to the 'students' relation
def addStudent(first_name, last_name, email, enrollment_date):
	
	try:
	
		# Checking to see if the first name, last name, or email are null + if email is unique
		if first_name.lower() == 'null' or last_name.lower() == 'null':
			print('\n')
			print("First and last names have to have values. Null values are not accepted. Student wasn't added.")
			return

		elif email.lower() == 'null':
			print('\n')
			print("Emails have to have values. Null values are not accepted. Student wasn't added.")
			return


		# This line excutes the INSERT query to add the student to the 'students' table
		c_obj.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)", (first_name, last_name, email, enrollment_date))

		# This commit line is there to save the changes to the database (and so is all other calls to commit() in the rest of the program)
		connector.commit()

	# This except block is for catching UniqueViolation exceptions (when the email of the student we are trying to add is not unique)
	except:
		print('\n')
		print("The email of the student you are trying to add is not unique. Student wasn't added.")
	

# Updates the email address of a student with the specified student_id in the 'students' relation
def updateStudentEmail(student_id, new_email):

	# This line excutes the UPDATE query to update the email of the student with the given student id to a new email equal to the given 'new_email' parameter
	c_obj.execute("UPDATE students SET email=" + '\'' + str(new_email) + '\'' + " WHERE student_id=" + str(student_id))

	# This commit line is there to keep the updated student email in the 'students' table after this program terminates
	connector.commit()

# Deletes the record of the student with specified student_id from the 'students' relation
def deleteStudent(student_id):

	# This line excutes the DELETE query to delete the student with the given student id from the 'students' table
	c_obj.execute("DELETE FROM students WHERE student_id=" + str(student_id))

	# This commit line is there to keep the added student in the 'students' table after this program terminates
	connector.commit()

# Main function for control flow
def main():
	
	while True:
	
		choice = input("Would you like to (1) get all the students in the 'students' table OR (2) add a student to the 'students' table OR (3) delete a student from the 'students' table OR (4) update a student's email address in the 'students' table OR (5) exit (type in either 1, 2, 3, 4, or 5)? ") 
	
		if choice == '1':
			print('\n')
			print("Here are the students in the 'students' table: ")
			print('\n')
			getAllStudents()
			print('\n')

		elif choice == '2':
			f = input("What's the student's first name? ")
			l = input("What's the student's last name? ")
			e = input("What's the student's email? ")
			ed = input("What's the student's enrollment date (type the date in this format: yyyy-mm-dd)? ")
			addStudent(f,l,e,ed)
			print('\n')
	
		elif choice == '3':
			id = int(input("What is the student's id? "))
			deleteStudent(id)
			print('\n')

		elif choice == '4':
			s_id = int(input("What is the student's id? "))
			new_mail = input("What will be the student's new email? ")
			updateStudentEmail(s_id, new_mail)
			print('\n')

		elif choice == '5':
			break

		else:
			print('Invalid value. Choose either 1, 2, 3, 4, or 5.')
			print('\n')

# Executing the 'main' function to start program control flow
main()
	