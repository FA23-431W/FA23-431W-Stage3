import sqlite3
from Game_Lib.game_lib import *

def admin_menu(conn, user_id):
    while True:
        print("\n----------- Admin Menu -----------")
        print("1. View")
        print("2. Insert")
        print("3. Delete")
        print("4. Update")
        print("5. Logout")
        print("----------- Admin Menu ------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            game_library_menu(conn, user_id)
        elif choice == "2":
            insert_menu(conn, user_id)
        elif choice == "3":
            delete_menu(conn, user_id)
        elif choice == "4":
            update_menu(conn, user_id)
        elif choice == "5":
            print("Logout")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = sqlite3.connect("Data/data.db")
    admin_menu(conn, "admin")
