from mysql.connector import connect
from passlib.hash import pbkdf2_sha256


cnx = connect(user="root", password="coderslab", host="localhost",
              database="logowanie_db")
cursor = cnx.cursor()


class User:

    __id = None
    username = None
    __hashed_password = None
    email = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password):
        self.__hashed_password = pbkdf2_sha256.encrypt(password, rounds=200000,
                                                       salt_size=16)

    def save_to_db(self, cursor = cursor):
        if self.__id == -1:
            # saving new instance using prepared statements
            sql = """INSERT INTO Users(username, email, hashed_password)
            VALUES(%s, %s, %s)"""
            values = (self.username, self.email, self.__hashed_password)
            cursor.execute(sql, values)
            cnx.commit()
            self.__id = cursor.lastrowid
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s
                     WHERE id=%s"""
            values = (self.username, self.email, self.__hashed_password,
                      self.__id)
            cursor.execute(sql, values)
            cnx.commit()
            return True

    def delete(self, cursor=cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.__id, ))
        cnx.commit()
        self.__id = -1
        return True


    @staticmethod
    def load_user_by_id(id, cursor=cursor):
        sql = "SELECT * FROM Users WHERE id = %s"
        result = cursor.execute(sql, (id, ))
        data = cursor.fetchone()

        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_name(name, cursor=cursor):
        sql = "SELECT * FROM Users WHERE username = %s"
        result = cursor.execute(sql, (name, ))
        data = cursor.fetchone()

        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor=cursor):
        sql = "SELECT * FROM Users"
        ret = []
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret


####### Zamknalem polaczenie dopiero w programie, czy tak bedzie ok?







# fname = "Prawysxcfgxcv"
# mail = "manvcxgfdzcxv@wp.pl"
# passw = "alamakota123"
# #
# #
# #
# abc = User()
# abc.username = fname
# abc.email = mail
# abc.set_password(passw)
# abc.save_to_db()
# print(abc._User__id)


#
# User.load_user_by_id(cursor, 1)
# print(User.load_user_by_id(cursor, 1))
#
#
# print(User.load_user_by_id(cursor, 1).email)
#
#
# print(User.load_all_users(cursor))

# for i in User.load_all_users(cursor):
#     print(i.email)


# user_id13 = User.load_user_by_id(2)
# user_id13.delete()


# print(User.load_user_by_name("Lewy"))
