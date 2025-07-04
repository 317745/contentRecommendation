from models.connection import *
from psycopg2.extras import RealDictCursor

def confirmUserNameEmailCode(email):
    try: 
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT email FROM codemail WHERE email = %s", (email, ))
        response = cursor.fetchone()
        
        if response is not None: 
            if response['email'] == email:
                return {
                    'ok': False,
                    'data': "A code has already been sent previously."
                }
            
        return {
            'ok': True,
            'data': "Thanks, an email was sent with the code."
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }