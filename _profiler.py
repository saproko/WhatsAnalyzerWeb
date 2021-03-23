import logging
import sys
import os
from os import path

basedir = path.dirname(path.realpath(__file__))
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, basedir)

from werkzeug.middleware.profiler import ProfilerMiddleware
from WhatsAnalyzerWeb import app as application
from flask_session import Session

application.secret_key = os.urandom(64)
application.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
application.config["SESSION_TYPE"] = "filesystem"
application.config["SESSION_FILE_DIR"] = path.join(basedir, "flask_session")
application.config["PROFILE"] = True
application.wsgi_app = ProfilerMiddleware(application.wsgi_app, restrictions=[30])
Session(application)

application.run(debug=True)