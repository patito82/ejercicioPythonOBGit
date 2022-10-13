import sqlite3

conexion = sqlite3.connect('Alumnos.db')
print('Open database')
conexion.execute('''create table if not exists alumnos
                (id integer primary key,
                nombre text,
                apellido text
                );''')
print('tabla create')
conexion.close()

try:
    conexion = sqlite3.connect('Alumnos.db')
    cursor = conexion.cursor()
    cursor.execute("""insert into alumnos (id,nombre,apellido)
    values
    (1, 'valen', 'chipa'),
    (2, 'valenti', 'chipa'),
    (3, 'valentin', 'chipa'),
    (4, 'vale', 'chipa'),
    (5, 'valu', 'chipa'),
    (6, 'pepe', 'chipa'),
    (7, 'juan', 'chipa'),
    (8, 'pedro', 'chipa')
    """)
    conexion.commit()
    cursor.close()
except sqlite3.IntegrityError as error:
    print("Ya esta agregado", error)
conexion.close()

conexion = sqlite3.connect('Alumnos.db')
cursor = conexion.cursor()
cursor.execute("select * from alumnos where nombre= 'valentin'")
alumno = cursor.fetchone()
print(alumno)
conexion.close()
