import mysql.connector as mysql

# To connect our Database
db = mysql.connect(host="localhost",user="root",password="",database="college")

# cursor funtion allows insert,delete and edit and so on
# buffer runs multiple queries without errors
command_handler = db.cursor(buffered=True)

def teacher_session():
    while 1:
          print("")
          print("Teacher's Register")
          print("")
          print("1. Mark Student Register")
          print("2. Register New Teacher")
          print("3. View Register")
          print("4. Logout")
          user_option = input(str("option : "))
          if user_option == "1":
           print("")
           print("Mark student Register")
           command_handler.execute(" SELECT username FROM users WHERE privilege = 'student' ")
# Fetch all the records from the query
           records = command_handler.fetchall()
           date    =    input(str("Date : DD/MM/YY : "))
           for record in records:
              record = str(record.replace("'",""))
              record = str(record.replace(",",""))
              record = str(record.replace("(",""))
              record = str(record.replace(")",""))
              # presrnt | late | absent
              status = input(str("status for" + str(records + "P/A/L : ")))
              query_values = (str(record),date,status)
              command_handler.execute = ("INSERT INTO attendance (username,date,status) VALUES(%s,%s,%s)",query_values)
              db.commit()
              print(record + "Marked as a" + status)










# This func is the menu once he or she logged in
def admin_session():
    while 1:
           print("")
           print("Admin Menu")
           print("")
           print("1. Register New Student")
           print("2. Register New Teacher")
           print("3. Delete Existing Student")
           print("4. Deleting Existng Teacher")
           print("5. Logout")
           user_option = input(str("Enter option : "))
           if user_option == "1":
            print("")
# Admin must provide username and login to the student this information going to store in a database in a second
            print("Register new student")
            username = input(str("student username : "))
            password = input(str("student password : "))
# Then we have to store the username and password
            query_vals = (username,password)
# Its going to run our command or query in database
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'student')",query_vals)
# Save all the changes to db
            db.commit()
            print(username,"has been registered as a student")

           elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'Teacher')",query_vals)
            db.commit()
            print(username,"has been registered as a Teacher")

           elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student Username : "))
# In This the account belongs to student(privilege)
            query_vals = (username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
# This if statements tells how many rows were affected
            if command_handler.rowcount < 1:
              print("User not found")
            else:
              print(username,"username has been deleted")

           if user_option == "4":
              print("")
              print("Delete Existing Teacher Account")
              username = input(str("Teacher Username : "))
              query_vals = (username,"Teacher")
              command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
              db.commit()
# This if statements tells how many rows were affected
              if command_handler.rowcount < 1:
                 print("User not found")
              else:
                print(username,"username has been deleted")
        
              if user_option == "5":
                break
                print("No valid option selected")
        
    
def auth_teacher():
               print("")
               print("Teacher's Login")
               print("")
               username = input(str("username : "))
               password = input(str("password : "))
               query_values = (username,password)
               command_handler.execute = ("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",query_values)
               if command_handler == 0:
                  print("Login not recognized")
               else:
                  teacher_session()


def auth_admin():
            print("")
            print("Admin Login")
            print("")
            username = input(str("username : "))
            password = input(str("password : "))
 
            if username == "admin":
                if password == "password":
# if user enters the correct password it will directed into admin_session()
                    admin_session()
                
                else: print("The password is incorrect..!!!!!!")
                
            else:
                print("Login does not recognized")
  
# This is the main()
def main():
    while 1:
            print("")
            print("welcome to the college system")
            print("")
            print("1. Login as Student")
            print("2. Login as Teacher")
            print("3. Login as Admin")

            user_option = input(str("Enter your option : "))
            if user_option == "1":
               print("Student login")
            elif user_option == "2":
               auth_teacher()
            elif user_option == "3":
# If user enter option3 it will directed into admin() 
               auth_admin()  
            else:   
                print("choose the correct option")

main()