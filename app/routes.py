from app import app
from flask import render_template
from app.models import Course

@app.route('/')
@app.route('/index')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)