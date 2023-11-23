# a4rep
Database setup instructions: Execute the three sql scripts in the "database_scripts" directory in the following order: database_creation.sql, table_creation.sql, and populate_table.sql (you can do this by uploading each file to pgadmin4 and running the file's code there).

Getting the application to run: since the application is written in python, you will need to have python installed in order to execute it (make sure your python version is at least 3.10.11, since that is the version I used to run the app). The file also uses an external module called "psycopg2" to interact with Postgres servers. To get this module, install it using pip3 (install command: pip3 install psycopg2).

Function descriptions:

getAllStudents(): This function gets all the tuples in the 'students' relation.

addStudent(first_name, last_name, email, enrollment_date): This function adds a student to the 'students' relation.

updateStudentEmail(student_id, new_email): This function updates the email of the student with the given student id.

deleteStudent(student_id): This function deletes the student with the given student id from the 'students' relation.

main(): This function controls the program's control flow.

