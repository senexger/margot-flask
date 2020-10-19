from flask import Flask

app = Flask(__name__)

# workaround to circular routines
from app import routes
