import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=get_decrypted_password(),
            database="test"
        )
        print("✅ Connected to MySQL successfully!")
        print(get_decrypted_password())
        conn.close()
    except mysql.connector.Error as err:
        print(f"Connection failed: {err}")

if __name__ == "__main__":
    connect_to_mysql()
