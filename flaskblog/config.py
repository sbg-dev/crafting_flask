import os

class config:
    SECRET_KEY = '8194320ea968946102e036d8e7ed4230'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
