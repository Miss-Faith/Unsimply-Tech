from flask import Flask
from config import config_options
# Initializing application
app = Flask(__name__)

from app.main import views