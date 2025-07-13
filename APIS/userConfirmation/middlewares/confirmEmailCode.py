from models.connection import *
from psycopg2.extras import RealDictCursor
from flask import jsonify

def confirmEmailCode(email):
    try: 
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT email FROM codemail WHERE email = %s", (email, ))
        response = cursor.fetchone()
        
        if response: 
            return jsonify({
                'ok': False,
                'data': 'A code has already been sent previously.'
            }), 409
            
        return jsonify({
            'ok': True,
            'data': 'Thanks, an email was sent with the code.'
        }), 200
    
    except Exception as e:
        return jsonify({
            'ok': False,
            'data': 'An error has happened searching the email.'
        }), 500