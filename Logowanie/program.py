from mysql.connector import connect
from user import User
import argparse


# Program do zarządzania użytkownikiem

parser = argparse.ArgumentParser()


parser.add_argument("-u", "--username", type=str,
                    dest="username", default=False, help="Username")
parser.add_argument("-p", "--password",
                    type=str, dest="password",
                    default=False, help="Password for username")
parser.add_argument("-n", "--new-pass",
                    action="store_true", dest="newpass",
                    default=False, help="Change the password if exist")
parser.add_argument("-l", "--list",
                    action="store_true", dest="list",
                    default=False, help="Display the all users")
parser.add_argument("-d", "--delete",
                    action="store_true", dest="delete",
                    default=False, help="Delete email")
parser.add_argument("-e", "--edit",
                    action="store_true", dest="edit",
                    default=False, help="Edit email")

args = parser.parse_args()

if args.username and args.password:
    print("OK")




cursor.close()
cnx.close()