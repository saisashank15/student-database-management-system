import pymysql

# Database credentials
host = 'localhost'
user = 'root'
password = 'sashank'
database = 'student_management'

# Establish a connection to the MySQL server
connection = pymysql.connect(host=host, user=user, password=password)

# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Select the database
cursor.execute(f"USE {database}")

# SQL statement to create the table
create_table_query = '''
CREATE TABLE student_register (
    f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    course VARCHAR(30) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    year INT(10) NOT NULL,
    age INT(10) NOT NULL,
    gender CHAR(10) NOT NULL,
    birth DATE NOT NULL,
    contact VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (contact)
)
'''

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Table 'student_register' created successfully.")
