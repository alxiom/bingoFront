# -*- coding: utf-8 -*-

from root import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('bingo.html')


@app.route('/play', methods=['GET', 'POST'])
def start():
    input_code = request.args.get('code')
    time_stamp = request.args.get('ts')
    return render_template('play.html', input_code=input_code, time_stamp=time_stamp)
