from models.connection import *
from middlewares.confirmEmailCode import *

import os 
import random
import smtplib
import requests

from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
from flask import request, jsonify
from psycopg2.extras import RealDictCursor
from datetime import datetime

load_dotenv()

def saveCode(code, localDate, emailAddres, username):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO codemail (
        code, date, email, username
        )
        VALUES (
        %s, %s, %s, %s)
        ''', (
            code, localDate, emailAddres, username
        ))
        conn.commit()
        return jsonify({
            'ok': True,
            'data': 'The data has been saving.'
        }), 200
    
    except Exception as e:
        return jsonify({
            'ok': False,
            'data': str(e)
        })
        

def sendEmail(emailAddres, username, localDate):
    string = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    array = [random.choice(string) + str(random.randint(0, 9)) for _ in range(5)]
    code = ''.join(array)

    if localDate is None:
        localDate = 'NOW()'

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
                            width: 60vh;
                            height: 40vh;
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
        
        responseSaveCode, statuSaveCode = saveCode(code, localDate, emailAddres, username)
        responseSaveCode = responseSaveCode.get_json()
        if not responseSaveCode['ok']:
            return jsonify(responseSaveCode), statuSaveCode

        return jsonify({
            'ok': True,
            'data': 'El correo con el codigo de confirmacion se ha enviado.',
        }), 200
    except Exception as e:
        return jsonify({
            'ok': False,
            'data': str(e)
        }), 200
        
def deleteOldCodes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM codemail
        WHERE NOW() - date > INTERVAL '5 MINUTE'
        ''')
        conn.commit()
        return jsonify({
            'ok': True, 
            'data': 'Se eliminaron correctamente los codigos anteriores.'
        }), 200
    except Exception as e:
        return jsonify({
            'ok': False,
            'data': str(e)
        }), 500
    
def verifySendCode():
    try:
        email = request.json.get('email')
        username = request.json.get('username')
        localDate = request.json.get('localdate')

        responseConfirmUserEmail = requests.post('http://localhost:3031/usernameEmailConfirmation',
                                           json={
                                               'username': username, 
                                               'email': email
                                           })
        statusCodeConfirmUserEmail = responseConfirmUserEmail.status_code
        responseConfirmUserEmail = responseConfirmUserEmail.json()
        if not responseConfirmUserEmail['ok']:
            print('I')
            return jsonify(responseConfirmUserEmail), statusCodeConfirmUserEmail
        
        responConfirmEmail, statusCodeConfirmEmail = confirmEmailCode(email)
        responConfirmEmail = responConfirmEmail.get_json()
        if not responConfirmEmail['ok']:
            print('II')
            return jsonify(responConfirmEmail), statusCodeConfirmEmail

        responSendEmail, statusCodeSendEmail = sendEmail(email, username, localDate)
        responSendEmail = responSendEmail.get_json()
        if  not responSendEmail['ok']:
            print('III')
            return jsonify(responSendEmail), statusCodeSendEmail

        return jsonify({
            'ok': True,
            'data': f'The code has been sendend to the email {email}'
        }), 200

    except Exception as e:
        print(e)
        return jsonify({
            'ok': False,
            'data': str(e),
            'error': 'IIII'
        }), 500
    
def checkCode():
    try:
        deleteOldCodesResponse, statusDeletOldCodes = deleteOldCodes()
        deleteOldCodesResponse = deleteOldCodesResponse.get_json()
        if not deleteOldCodesResponse['ok']:
            return jsonify(deleteOldCodesResponse), statusDeletOldCodes
        
        code = request.json.get('code')
        email = request.json.get('email')

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('''
        SELECT * 
        FROM codemail
        WHERE code = %s AND email = %s''',
        (code, email))

        response = cursor.fetchone()
        if response is None:
            return jsonify({
                'ok': False, 
                'data': f'The code {code} is not valid. Please confirm.'
            })
        
        for key, value in response.items():
            if key == 'date':
                response.update({
                    key: f'{value.strftime('%Y-%m-%d %-I:%M:%S %p')}'
                    })
                
        return jsonify({
            'ok': True,
            'data': response
        }), 200
    except Exception as e:
        return jsonify({
            'ok':False, 
            'data': str(e)
        }), 500