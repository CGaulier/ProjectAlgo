import pandas as pd
import numpy as np
import scipy as sp
import sklearn
import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask

app = Flask(__name__)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@app.route('/')
def hello_world():
    return render_template('home.html')