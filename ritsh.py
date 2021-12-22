import mysql.connector as database

#connection = database.connect(
 #              user="root",
 #              password="password",
 #              host="localhost",
 #              database="office",
 #              port="3306"
#
#             )
#cursor = connection.cursor()
#add_user = """INSERT INTO office.Persons
#             (PersonID, LastName, FirstName, Address , City) 
 #            VALUES (%s,%s,%s,%s,%s)"""
#data_user = ('1201', 'pal', 'rat','no admin', 'bst')
#cursor.execute(add_user, data_user)
#connection.commit()
#cursor.close()
#connection.close()
#print("Successfully added entry to database")

#add_user1 = """INSERT INTO office.Persons
          #   (PersonID, LastName, FirstName, Address , City)
           #  VALUES (%s,%s,%s,%s,%s)"""
connection1 = database.connect(
               user="root",
               password="password",
               host="localhost",
               database="office",
               port="3306"

             )

cursor1  = connection1.cursor()
add_user = """INSERT INTO office.Persons
             (PersonID, LastName, FirstName, Address , City)
             VALUES (%s,%s,%s,%s,%s)"""
data_user1 = ('1231', 'singh', 'ritesh','admin', 'gkp')
cursor1.execute(add_user, data_user1)
connection1.commit()
cursor1.close()
connection1.close()
print("Successfully added entry to database")
