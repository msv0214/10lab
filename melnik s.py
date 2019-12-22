import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_config(conn):
    sql = 'SELECT * FROM melnik'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_config(conn, task):
    sql = ''' INSERT INTO melnik (config, value)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


def update_config(conn, data):
    sql = ''' UPDATE melnik
              SET value = ?
              WHERE config = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def remove_config(conn, removed_task):
    sql = ''' DELETE FROM melnik WHERE config = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


def main():

    database = r"melnik s.db" 
 
    conn = create_connection(database)

    with conn:
        print("\nВсі нотатки (текст, дата)")
        select_config(conn)
        print("\nВставка нового рядка...")
        create_config(conn, ('Останнє збереження', '20,12,2019'))
        print("\nВсі нотатки (текст, дата)")
        select_config(conn)
        print("\nЗміна рядка...")
        update_config(conn, ('21,12,2019', 'Останнє збереження'))
        print("\nВсі нотатки (текст, дата)")
        select_config(conn)
        print("\nВидалення рядка")
        remove_config(conn, ('Останнє збереження',))
        print("\nВсі нотатки (текст, дата)")
        select_config(conn)
        
 
if __name__ == '__main__':
    main()
