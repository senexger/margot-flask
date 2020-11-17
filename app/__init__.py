from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# workaround to circular routines
from app import routes
