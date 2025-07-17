from flask_mail import Message
from flask import url_for, current_app
from . import mail
import threading

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_verification_email(user):
    token = "dummy-token"
    msg = Message("Verify Your Email", recipients=[user.email])
    msg.html = f'''
        <h3>Welcome!</h3>
        <p>Please click the link below to verify your account:</p>
        <a href="{url_for('auth.login', _external=True)}">Verify</a>
    '''
    thread = threading.Thread(target=send_async_email, args=(current_app._get_current_object(), msg))
    thread.start()