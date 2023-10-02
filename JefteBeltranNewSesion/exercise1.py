import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database = "prueba"

)

print(mydb)

# mycursor = mydb.cursor() 
# mycursor.execute("create databse new_prueba")


#verificar que base de datos existen
#mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")



#for databses in mycursor:
   # print(databses)



mycursor = mydb.cursor()

#mycursor.execute('CREATE TABLE students(fname VARCHAR(50), lname VARCHAR(30), score INT)')





#mycursor.execute("CREATE TABLE info ( id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(50), lname VARCHAR(30), score INT)")



mycursor.execute('SHOW TABLES')

for it in mycursor:
    print(it)


#AGREGANDO UNA CLAVE PRIMARIA A UNA TABLA YA CREADA

#mycursor.execute('ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

#------------------AGREGANDO UN REGISTRO-----------------------
sql = 'INSERT INTO students(fname, lname, score) VALUES(%s,%s,%s)'
val = ('John','Doe', '10')

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, 'registro insertado')



#---------------------------AGREGANDO VARIOS REGISTROS---------------------------------------
import random

# Listas de nombres y apellidos ficticios
"""
nombres = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "Daniel", "Sophia", "David", "Emma"]
apellidos = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson"]

# Generar 40 tuplas aleatorias
tuplas = []
for _ in range(40):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nota = random.randint(0, 10)
    tupla = (nombre, apellido, nota)
    tuplas.append(tupla)



sql = "INSERT INTO students (fname, lname, score) VALUES(%s,%s,%s)"
val = tuplas

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,'registro insertado')

"""

#---------------SELECCIONAR TODOS LOS ELEMENTOS DE UNA TABLA------------------------
mycursor.execute('SELECT * FROM students')

myresult = mycursor.fetchall()

for it in myresult:
    print(it)
#mydb.close()


