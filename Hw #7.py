import sqlite3
db=sqlite3.connect('student.db')
c=db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
Фамилия TEXT,
Имя TEXT, 
Год INTEGER,
Баллы INTEGER
)''')

c.execute('SELECT * FROM student WHERE LENGTH(Фамилия) > 10')
students = c.fetchall()

for student in students:
    print(student)

c.execute('UPDATE student SET Имя="genius" WHERE Баллы = 10')
c.execute('SELECT * FROM student WHERE Баллы=10')
geniuses = c.fetchall()

for geniuse in geniuses:
    print(geniuse)

c.execute('DELETE FROM student WHERE id IN (2, 4, 6, 8, 10)')

db.commit()
db.close()
