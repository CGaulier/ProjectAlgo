import pandas as pd
import numpy as np
import scipy as sp
import sklearn
import flask
import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('webInterface/home.html')