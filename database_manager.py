import psycopg2


class DB:

    def store_passwords(self,password, user_email, username, url, app_name):
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
            record_to_insert = (password, user_email, username, url, app_name)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)

    def connect(self):
        try:
            connection = psycopg2.connect(user='postgres', password='Passroot112', host='127.0.0.1', database='password_manager')
            return connection
        except (Exception, psycopg2.Error) as error:
            print(error)

    def find_password(self,app_name):

        data = ('Id','Password: ', 'E-mail: ', 'Username: ', 'url_site: ', 'Site name: ')
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_select_query = """ SELECT * FROM accounts WHERE app_name = '""" + app_name + "'"
            cursor.execute(postgres_select_query, app_name)
            connection.commit()
            result = cursor.fetchall()
            print('')
            print('RESULT')
            print('')
            for row in result:
                for i in range(1, len(row)):
                    print(data[i] + row[i])
                print('______________')
            print('')
            print('-' * 30)
        except (Exception, psycopg2.Error) as error:
            print(error)
    def find_users(self,user_email):
        data = ('Id', 'Password: ', 'E-mail: ', 'Username: ', 'url_site: ', 'Site name: ')
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
            cursor.execute(postgres_select_query, user_email)
            connection.commit()
            result = cursor.fetchall()
            print('')
            print('RESULT')
            print('')
            for row in result:
                for i in range(1, len(row)):
                    print(data[i] + row[i])
                print('______________')
            print('')
            print('-'*30)
        except (Exception, psycopg2.Error) as error:
            print(error)

    def show_accounts(self):
        data = ('Id','Password: ', 'E-mail: ', 'Username: ', 'url_site: ', 'Site name: ')
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_select_query = """ SELECT * FROM accounts"""
            cursor.execute(postgres_select_query)
            connection.commit()
            result = cursor.fetchall()
            print('')
            print('RESULT')
            print('')
            for row in result:
                for i in range(1, len(row)):
                    print(data[i] + row[i])
                print('______________')
            print('')
            print('-' * 30)
        except (Exception, psycopg2.Error) as error:
            print(error)

    def fast_dump(self):
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_select_query = """ SELECT * FROM accounts"""
            cursor.execute(postgres_select_query)
            connection.commit()
            result = cursor.fetchall()
            print('')
            print('RESULT')
            print('')
            with open("dump.txt","w") as f:
                for row in result:
                    f.write(str(row))
                    f.write("\n")

        except (Exception, psycopg2.Error) as error:
            print(error)

    def delete_entry(self,user_email,app_name):
        try:
            connection = DB().connect()
            cursor = connection.cursor()
            postgres_insert_query = f"""DELETE from accounts where email='{user_email}' and app_name='{app_name}';"""
            cursor.execute(postgres_insert_query)
            connection.commit()
            connection.close()
            print("Entry was deleted!")

        except (Exception, psycopg2.Error) as error:
            print(error)
