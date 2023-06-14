import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = os.environ.get('DEBUG_MODE')
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = os.environ.get('DEBUG_MODE')
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

'''
class dbConfig():
    def dbConnect(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
        db = SQLAlchemy()
        print("DB config : ", db)
        return db
        ''''''
        with app.app_context():
            try:
                stTest = db.session.execute(text('SELECT 1'))
                print("[+] DATABASE CONNECTED : ", str(stTest.first()))
                print("[+] ENGINE : ", db.engine.name)
                print("[+] DRIVER : ", db.engine.driver)
                print("[+] URL : ", db.engine.url)
                print("DB : ", db)
                #return db
            except Exception as e:
                print("[-] DATABASE ERROR !!!", str(e))
                return e
                '''''
        #return db