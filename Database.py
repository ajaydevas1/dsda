import mysql.connector

#make sure you written everthing write
#install mysql.connector through(pip install mysql-connector-python)
#its here till we have new project help me out in that 
#call me out if to make change in this file 
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    port=3306,
    database='your_databse'
)
cursor = conn.cursor()

#its worked on my databse 
def read_data(cursor, conn):
    query = "SELECT * FROM student;"
    cursor.execute(query)
    table = cursor.fetchall()
    for row in table:
        print(row)

#change the values according to your table and databse
def add_new_details(cursor, conn):
    try:
        rno = int(input("Enter Roll No. of New student ...Check in Database before inserting new details: "))
        sname = input("Enter student name: ")
        coursename = input("Enter course name: ")  # New column
        query = f"INSERT INTO student VALUES ({rno}, '{sname}', '{coursename}');"
        cursor.execute(query)
        conn.commit()
        print("Inserted successfully!")
    except Exception as e:
        conn.rollback()
        print("Error inserting data:", e)

def update_details(cursor, conn):
    try:
        inn = input("What do you want to update ('rno', 'sname', or 'course_name'): ")

        if inn == 'rno':
            print("IN RNO UPDATION")
            give = input("Give the WHERE condition: ")
            rn = input("Enter the new RNO: ")
            query = f"UPDATE student SET rno = {rn} WHERE sname = '{give}';"
            cursor.execute(query)
            conn.commit()
            print("UPDATED")

        elif inn == 'sname':
            print("IN SNAME UPDATION")
            where = input("Give the WHERE condition: ")
            sname = input("Enter the new SNAME: ")
            query = f"UPDATE student SET sname = '{sname}' WHERE rno = {where};"
            cursor.execute(query)
            conn.commit()
            print("UPDATED")

        elif inn == 'course_name':  # New column
            print("IN COURSENAME UPDATION")
            where = input("Give the WHERE condition: ")
            coursename = input("Enter the new COURSENAME: ")
            query = f"UPDATE student SET course_name = '{coursename}' WHERE rno = {where};"
            cursor.execute(query)
            conn.commit()
            print("UPDATED")

        else:
            print("Invalid option. Please try again.")

    except Exception as e:
        conn.rollback()
        print("An error occurred:", e)

def add_column(cursor, conn):
    try:
        column_name = input("Enter the name of the new column: ")
        data_type = input("Enter the data type of the new column: ")
        query = f"ALTER TABLE student ADD COLUMN {column_name} {data_type};"
        cursor.execute(query)
        conn.commit()
        print("Column added successfully!")
    except Exception as e:
        conn.rollback()
        print("Error adding column:", e)

def delete_user(cursor, conn):
    try:
        rno = int(input("Enter the Roll No. of the student to delete: "))
        query = f"DELETE FROM student WHERE rno = {rno};"
        cursor.execute(query)
        conn.commit()
        print("User deleted successfully!")
    except Exception as e:
        conn.rollback()
        print("Error deleting user:", e)

def delete_column(cursor, conn):
    try:
        column_name = input("Enter the name of the column to delete: ")
        query = f"ALTER TABLE student DROP COLUMN {column_name};"
        cursor.execute(query)
        conn.commit()
        print("Column deleted successfully!")
    except Exception as e:
        conn.rollback()
        print("Error deleting column:", e)

#ruining in while loop until the statement is wrong
while True:
    print("\n1. Read Details in Database")
    print("2. Insert Details in Database")
    print("3. Update a detail in Database")
    print("4. Add a new column")
    print("5. Delete a user")
    print("6. Delete a column")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        read_data(cursor, conn)
    elif choice == '2':
        add_new_details(cursor, conn)
    elif choice == '3':
        update_details(cursor, conn)
    elif choice == '4':
        add_column(cursor, conn)
    elif choice == '5':
        delete_user(cursor, conn)
    elif choice == '6':
        delete_column(cursor, conn)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1-7")

cursor.close()
conn.close()
