# -*- coding: utf-8 -*-
import os, time
import loader
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

DATA = loader.getFullSchedule()
db = SQLAlchemy(app)


class Counts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.String(11))
    count = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    return redirect(url_for('home', language='kz'))


@app.route('/home')
def home():
    current_day = time.strftime('%A')
    language = getLanguage(request.args.get('language'))
    grade, data = getData(request.args.get('grade'))
    check(session)
    return render_template('home.html', grades=sorted(list(DATA.keys())), data=data, current_day=current_day, grade=grade, language=language, translation=loader.TRANSLATION, attendance=getTotal(), i=0)


@app.route('/history')
def history():
    return render_template('hist.html', table=Counts.query.order_by(Counts.id.desc()), i=1)


@app.errorhandler(404)
def not_found(e): 
    return render_template("error.html", i=1) 


def getTotal():
    total = Counts.query.all()
    return sum(list(map(lambda d: d.count, total)))


def getData(grade):
    if grade in DATA:
        return grade, DATA[grade]
    return None, None


def check(session):
    if 'visited' not in session:
        session['visited'] = 1
        date = time.strftime('%d/%m/%Y')
        tmp = Counts.query.filter_by(dt=date).first()
        if tmp:
            tmp.count += 1
        else:
            new = Counts(dt=date,count=1)
            db.session.add(new)
        db.session.commit()


def getLanguage(lang):
    if lang not in ['eng', 'ru', 'kz']:
        lang = 'kz'
    return lang
    

if __name__ == '__main__':
    app.run()