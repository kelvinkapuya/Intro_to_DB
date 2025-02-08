import mysql.connector
from mysql.connector import Error

def create_database():
        try:
                    # Connect to MySQL server (update credentials as needed)
                            connection = mysql.connector.connect(
                                                host="localhost",
                                                            user="your_username",
                                                                        password="your_password"
                                                                                )

                                    if connection.is_connected():
                                                    cursor = connection.cursor()
                                                                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                                                                            print("Database 'alx_book_store' created successfully!")

                                                                                except mysql.connector.Error as e:  # Specific error handling for MySQL
                                                                                            print(f"Error: {e}")

                                                                                                finally:
                                                                                                            # Close the connection
                                                                                                                    if 'cursor' in locals():
                                                                                                                                    cursor.close()
                                                                                                                                            if 'connection' in locals() and connection.is_connected():
                                                                                                                                                            connection.close()

                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                    create_database()

