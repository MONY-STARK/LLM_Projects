import sqlite3

# Create a connection to the SQLite database (or create the file if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'students' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name varchar(50) ,
        class varchar(50),
        section varchar(50),
        rank int
    );
''')

# Insert some sample data into the 'students' table
cursor.executemany('''
    INSERT INTO students (name, class, section, rank) VALUES (?, ?, ?, ?);
''', [
    ('Alice', 'Data Science', 'A', 1),
    ('Bob', 'Computer Science', 'B', 2),
    ('Charlie', 'Mathematics', 'C', 3),
    ('David', 'Physics', 'A', 4),
    ('Eve', 'Data Science', 'B', 5),
    ('Frank', 'Engineering', 'C', 6),
    ('Grace', 'Data Science', 'A', 7),
    ('Hannah', 'Computer Science', 'A', 8),
    ('Ian', 'Mathematics', 'B', 9)
])

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Database and table created, and data inserted successfully!")
