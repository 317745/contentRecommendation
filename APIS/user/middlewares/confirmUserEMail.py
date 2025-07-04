from models.connection import *
from psycopg2.extras import RealDictCursor

def confirmUserNameEmail(username, email):
    try: 
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT username, email FROM users WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()
        print(user)
        if user is not None:
            if user['username'] == username:
                return {
                    'ok': False,
                    'data': f"There's another user with the username {username}"
                }
            elif user['email'] == email:
                return {
                    'ok': False,
                    'data': f"There's another user with the email {email}"
                }
        return {
            'ok': True,
            'data': f"The username {username} and email {email} is available"
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }