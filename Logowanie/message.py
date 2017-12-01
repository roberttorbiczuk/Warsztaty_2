from mysql.connector import connect
from datetime import datetime

cnx = connect(user="root", password="coderslab", host="localhost",
              database="logowanie_db")
cursor = cnx.cursor()


class Message:

    __id = None
    user_id = None
    to_id = None
    mtext = None
    creation_date = None

    def __init__(self):
        self.__id = -1
        self.user_id = 0
        self.to_id = 0
        self.mtext = 0
        self.creation_date = datetime.today().date()

    @property
    def id(self):
        return self.__id

    # save record to db
    def save_to_db(self, cursor=cursor):
        if self.__id == -1:
            # saving new instance using prepared statements
            sql = """INSERT INTO Messages(user_id, to_id, mtext, 
                     creation_date) VALUES(%s, %s, %s, %s)"""
            values = (self.user_id, self.to_id, self.mtext, self.creation_date)
            cursor.execute(sql, values)
            cnx.commit()
            self.__id = cursor.lastrowid
            return True
        else:
            return False

    # delete record from database is exist
    def delete(self, cursor):
        sql = "DELETE FROM Messages WHERE id=%s"
        cursor.execute(sql, (self.__id, ))
        cnx.commit()
        self.__id = -1
        return True

    @staticmethod
    def load_all_messages_for_user(id, cursor=cursor):
        sql = """SELECT * FROM Messages LEFT JOIN Users ON 
                 Users.id=Messages.user_id WHERE Users.id = %s;"""
        list_of_messages = []
        cursor.execute(sql, (id,))
        results = cursor.fetchall()

        for row in results:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.user_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.mtext = row[3]
            loaded_message.creation_date = row[4]
            list_of_messages.append(loaded_message)
        return list_of_messages

    @staticmethod
    def load_message_by_id(id, cursor=cursor):
        sql = "SELECT * FROM Messages WHERE id = %s"
        result = cursor.execute(sql, (id, ))
        data = cursor.fetchone()
        if data is not None:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.user_id = data[1]
            loaded_message.to_id = data[2]
            loaded_message.mtext = data[3]
            loaded_message.creation_date = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_messages(cursor=cursor):
        sql = """SELECT * FROM Messages"""
        list_of_messages = []
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.user_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.mtext = row[3]
            loaded_message.creation_date = row[4]
            list_of_messages.append(loaded_message)
        return list_of_messages


# message = Message()
# message.user_id = 5
# message.to_id = 8
# message.mtext = "Hello World!"
# message.save_to_db()
# print(message.id)

# print(Message.load_all_messages())
# print(Message.load_message_by_id(6))
# print(Message.load_all_messages_for_user(5))


