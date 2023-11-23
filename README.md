# a4rep
Database setup instructions: Execute the three sql scripts in the "database_scripts" directory in the following order: database_creation.sql, table_creation.sql, and populate_table.sql (you can do this by uploading each file to pgadmin4 and running the file's code there).

Getting the application to run: since the application is written in python, you will need to have python installed in order to execute it (make sure your python version is at least 3.10.11, since that is the version I used to run the app). The file also uses an external module called "psycopg2" to interact with Postgres servers. To get this module, install it using pip3 (install command: pip3 install psycopg2). Finally, to run the application, navigate to the location of the application on your computer and use python to execute it (I tested it on windows and all I had to do was type in the file name and my operating system already knew which version of python to use to run my application).

Function descriptions:

getAllStudents(): This function gets all the tuples in the 'students' relation.

addStudent(first_name, last_name, email, enrollment_date): This function adds a student to the 'students' relation.

project demonstration (video): https://www.youtube.com/watch?v=Fr1l5OyTgOM

updateStudentEmail(student_id, new_email): This function updates the email of the student with the given student id.

deleteStudent(student_id): This function deletes the student with the given student id from the 'students' relation.

main(): This function controls the program's control flow.

