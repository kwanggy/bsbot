import os
basedir = os.path.abspath(os.path.dirname(__file__))

MOCK_DB_URI = 'sqlite:///' + os.path.join(basedir, 'mock.db')
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
