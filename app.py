import pandas as pd
import numpy as np
import scipy as sp
import sklearn
import flask

@bp.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('webInterface/home.html')