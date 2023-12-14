import mysql.connector

# Replace these values with your database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ankita16@02',
    'database': 'trail'
}

# Create a connection
conn = mysql.connector.connect(**db_config)

# Create a cursor
cursor = conn.cursor()
print("Choose an option:")
print("1. Read from database")
print("2. Insert into database")
print("3. Update database entry")
print("4. Delete from database")
print("5. Exit")

while True:
   
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Read from the database
        query = "SELECT * FROM try"
        cursor.execute(query)
        for row in cursor:
            print(row)
        print("Inserted Successfully")    
    
    elif choice == '2':
        # Insert into the database
        id=input("Entre Your ID : ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        query = "INSERT INTO try (id,name, age) VALUES (%s,%s, %s)"
        cursor.execute(query, (id,name, age))
        conn.commit()
        print("Data inserted successfully.")
    
    elif choice == '3':
        # Update a database entry
        id_to_update = input("Enter the ID of the entry to update: ")
        new_age = input("Enter the new age: ")
        query = "UPDATE try SET age = %s WHERE id = %s"
        cursor.execute(query, (new_age, id_to_update))
        conn.commit()
        print("Data updated successfully.")
    
    elif choice == '4':
        # Delete from the database
        id_to_delete = input("Enter the ID of the entry to delete: ")
        query = "DELETE FROM try WHERE id = %s"
        cursor.execute(query, (id_to_delete,))
        conn.commit()
        print("Data deleted successfully.")
    
    elif choice == '5':
        # Exit the program
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")

# Close the cursor and the connection
cursor.close()
conn.close()





sudo apt upda
te
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
sudo apt install python3
sudo apt install python3-pip
pip3 install mysql-connector-python

sudo mysql -u root -p
CREATE DATABASE yourdb;
CREATE USER 'youruser'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON yourdb.* TO 'youruser'@'localhost';
FLUSH PRIVILEGES;

USE yourdb;  -- Switch to the 'yourdb' database
CREATE TABLE your_table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
INSERT INTO your_table_name (name) VALUES
    ('swarada'),
    ('shravani'),
    ('vaishnavi'),
    ('yashashwi'),
    ('datta'),
    ('jyot');

EXIT;

import mysql.connector

# Define the connection parameters
config = {
    'user': 'youruser',
    'password': 'yourpassword',
    'host': 'localhost',
    'database': 'yourdb'
}

# Create a connection to the MySQL server
conn = mysql.connector.connect(**config)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Example: Execute a SQL query
cursor.execute("SELECT * FROM your_table_name")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close cursor and connection
cursor.close()
conn.close()

python3 -m venv myenv
source myenv/bin/activate
pip install mysql-connector-python

python3 your_script.py