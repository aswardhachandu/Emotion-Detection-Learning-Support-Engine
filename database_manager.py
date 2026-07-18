import mysql.connector

def add_user(email, name, password, username):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Muttukuri@44",  # Replace with your actual password
            database="emotion_db"
        )
        cursor = conn.cursor()
        
        # This matches your exact column list
        sql = "INSERT INTO users (email, name, password, username) VALUES (%s, %s, %s, %s)"
        val = (email, name, password, username)
        
        cursor.execute(sql, val)
        conn.commit()
        
        print(f"User {name} added successfully!")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Now providing all 4 required fields
    add_user("chandu@example.com", "Chandu Name", "secret123", "chandu_user")
def add_emotion_record(email, input_text, predicted_emotion):
    try:
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="emotion_db")
        cursor = conn.cursor()
        sql = "INSERT INTO emotion_records (email, input_text, predicted_emotion) VALUES (%s, %s, %s)"
        cursor.execute(sql, (email, input_text, predicted_emotion))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error saving emotion: {e}")