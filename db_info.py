import psycopg2


"""
1. install postgres
2.Open the command prompt and go to the directory where PostgreSQL is installed.
 Go to the bin directory and execute the following command to create a database.
createdb -h localhost -p 5432 -U postgres password_manager
3. Start the server:
pg_ctl -D "C:\Program Files\PostgreSQL\13\data" start/stop/restart
4. Crate table in password_manager DB
5.Done!


"""


def create_table():
    conn = psycopg2.connect(user='postgres', password="pass", host='127.0.0.1', database='password_manager')
    print("Opened database successfully")
    #
    cur = conn.cursor()
    cur.execute('''CREATE TABLE accounts
          (
          id SERIAL,
          password           TEXT    NOT NULL,
          email        CHAR(50),
          username        CHAR(50),
          url        CHAR(50),
          app_name         CHAR(50));''')
    conn.commit()
    conn.close()
    print("Table created successfully")

def test_insert():
    conn = psycopg2.connect(user='postgres', password="pass", host='127.0.0.1', database='password_manager')
    cur = conn.cursor()
    postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES ('test1', 'mail', 'user', 'url', 'app')"""
    cur.execute(postgres_insert_query)
    conn.commit()
    conn.close()
    print("Insert done!")

