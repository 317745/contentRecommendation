from models.connection import *
from models.confirmUserEmailCode import *

import os 
import random
import smtplib

from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
from flask import request, jsonify

load_dotenv()

def saveCode(code, emailAddres, username):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO codemail (
        code, date, email, username
        )
        VALUES (
        %s, NOW(), %s, %s)
        ''', (
            code, emailAddres, username
        ))
        conn.commit()
        print('Voy super zorras')
        return jsonify({
            'ok': True,
            'data': 'The data has been saving.'
        }), 200
    
    except Exception as e:
        print('me cai zorras', e)
        raise Exception('An error has happened saving the data.')
        

def sendEmail(emailAddres, username):
    string = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    array = [random.choice(string) + str(random.randint(0, 9)) for _ in range(5)]
    code = ''.join(array)

    remitente = os.getenv('GMAIL_USER')

    try: 
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = emailAddres
        email["Subject"] = 'Codigo de confirmacion.'
        email.set_content(f'''
           <html>
                <body style=" 
                            text-align: center;
                            margin: 5vh;
                            background-color: #424242;
                            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                            ">
                    <img src="https://raw.githubusercontent.com/317745/contentRecommendation/refs/heads/main/WEB/images/image.png" alt="Logo"
                        style="margin: 0vh 0vh 5vh 0vh;">
                    <h1 style="color: #fff;
                                margin: 0vh 0vh 5vh 0vh;">Bienvenido usuarios {username}. Este es tu codigo de confirmacion</h1>
                    <h2 style="color: #fff;
                                margin: 0vh 0vh 5vh 0vh;">{code}</h2>
                </body>
            </html>
        ''', subtype='html')

        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(remitente, os.getenv('GMAIL_APPKEY'))
        smtp.send_message(email)
        smtp.quit()
        
        saveCode(code, emailAddres, username)

        print('Me ejecute zorras')
        return jsonify({
            'ok': True,
            'data': 'El correo con el codigo de confirmacion se ha enviado.'
        }), 200
    except Exception as e:
        raise Exception('An error has happened sending the email.')
        
    
def verifySendCode():
    try:
        email = request.json.get('email')
        username = request.json.get('username')
        
        responConfirmEmail, statusCode = confirmEmailCode(email)
        responConfirmEmail = responConfirmEmail.get_json()
        if not responConfirmEmail['ok']:
            return jsonify(responConfirmEmail), statusCode

        responSendEmail, statusCode = sendEmail(email, username)
        responSendEmail = responSendEmail.get_json()

        
        return jsonify({
            'ok': True,
            'data': f'The code has been sendend to the email {email}'
        }), 200

    except Exception as e:
        return jsonify({
            'ok': False,
            'data': str(e)
        }), 500