from WhatsAnalyzerWeb import app as application
from flask_session import Session

from os import path
import os

basedir = path.dirname(path.realpath(__file__))
application.secret_key = os.urandom(64)
application.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
application.config["SESSION_TYPE"] = "filesystem"
application.config["SESSION_FILE_DIR"] = path.join(basedir, "flask_session")
Session(application)

application.run()