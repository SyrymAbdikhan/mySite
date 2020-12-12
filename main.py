import os, time, loader
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

DATA = {'11А': loader.getSchedule('static/schedules/11A'), '11Ғ': loader.getSchedule('static/schedules/11G\'')}
db = SQLAlchemy(app)


class Counts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.String(11))
    count = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    return redirect(url_for('home', language='kz'))


@app.errorhandler(404)
def not_found(e): 
    return render_template("error.html", i=1) 


@app.route('/history')
def history():
    return render_template('hist.html', table=Counts.query.order_by(Counts.id.desc()), i=1)


@app.route('/home')
def home():
    day = time.strftime('%A')
    lang = getLanguage(request.args.get('language'))
    grade, schedule, links, timetable = getData(request.args.get('grade'))
    check(session)
    return render_template('home.html', schedule=schedule, links=links, timetable=timetable, today=day, grade=grade, lang=lang, translation=loader.TRANSLATION, attendance=getTotal(), i=0)


def getTotal():
    total = Counts.query.all()
    return sum(list(map(lambda d: d.count, total)))


def getData(grade):
    if grade in DATA:
        return grade, *DATA[grade], loader.TIMETABLE
    return None, None, None, None


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