import os 
import random
import smtplib

from models.connection import *

from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def sendEmail(id, emailAddres):
    string = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    array = [random.choice(string) + str(random.randint(0, 9)) for _ in range(5)]
    code = ''.join(array)

    mensaje = f'''HOLA TE AMO, SOY TU ENAMORADO SECRETO UWU'''
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
                    <img src="https://raw.githubusercontent.com/317745/contentRecommendation/refs/heads/main/WEB/images/image.png" alt="zorra"
                        style="margin: 0vh 0vh 5vh 0vh;">
                    <h1 style="color: #fff;
                                margin: 0vh 0vh 5vh 0vh;">Este es tu codigo de confirmacion</h1>
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
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO codemail (
        id, code, date, email
        )
        VALUES (
        %s, %s, NOW(), %s)
        ''', (
            id, code, emailAddres
        ))
        conn.commit()
        print({
            'ok': True,
            'data': 'El correo con el codigo de confirmacion se ha enviado.'
        })
        return 
    except Exception as e:
        print({
            'ok': False,
            'data': str(e)
        })
        return {
            'ok': False,
            'data': str(e)
        }